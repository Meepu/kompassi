import logging
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timedelta

from django.db.models import QuerySet
from django.utils.timezone import get_current_timezone

from core.models import Event
from programme.models.category import Category
from programme.models.programme import PROGRAMME_STATES_LIVE, Programme
from programme.models.room import Room
from programme.models.tag import Tag

from ..consts import (
    CATEGORY_DIMENSION_TITLE_LOCALIZED,
    DATE_DIMENSION_TITLE_LOCALIZED,
    DEFAULT_COLORS,
    ROOM_DIMENSION_TITLE_LOCALIZED,
    TAG_DIMENSION_TITLE_LOCALIZED,
    WEEKDAYS_LOCALIZED,
)
from ..models.dimension import DimensionDTO, DimensionValueDTO, ProgramDimensionValue
from ..models.program import Program
from ..models.schedule import ScheduleItem

logger = logging.getLogger("kompassi")
tz = get_current_timezone()


@dataclass
class DefaultImporter:
    """
    The default importer for Kompassi V1 program items.
    Subclass this to implement custom import logic.
    The methods you usually want to reimplement are `get_program_dimension_values` and `build_dimensions`.
    If you need to change the way programs are imported, you can reimplement `get_program`, `get_schedule_items`, `get_length`, `get_start_time`, and `get_end_time`.
    If you are thinking you need to reimplement `import_program`, there are probably dragons.
    """

    event: Event
    language: str = "fi"

    date_cutoff_time = timedelta(hours=4)  # 04:00 local time

    def get_date_dimension_value(self, programme: Programme) -> str:
        """
        Return the date dimension value for the programme.

        The `date_cutoff_time` is used to determine at which time of the night the date changes.
        Use this to make the wee hours of the night belong to the previous day.
        """
        if not programme.start_time:
            raise ValueError(f"Programme {programme} has no start time")

        return (programme.start_time.astimezone(tz) - self.date_cutoff_time).date().isoformat()

    def _get_date_dimension_values(self) -> Iterable[DimensionValueDTO]:
        """
        Return a list of DimensionValueDTOs for the date dimension.
        """
        if not self.event.start_time:
            raise ValueError(f"Event {self.event} has no start time")
        if not self.event.end_time:
            raise ValueError(f"Event {self.event} has no end time")

        cur_date = self.event.start_time.astimezone(tz).date()
        end_date = self.event.end_time.astimezone(tz).date()

        while cur_date <= end_date:
            yield DimensionValueDTO(
                slug=cur_date.isoformat(),
                title={self.language: WEEKDAYS_LOCALIZED[self.language][cur_date.weekday()]},
            )
            cur_date += timedelta(days=1)

    def get_dimensions(self) -> list[DimensionDTO]:
        """
        Return a list of DimensionDTOs for the event.
        Don't call `DimensionDTO.save_many` on them, as this method is called by the importer.
        """
        return [
            DimensionDTO(
                slug="date",
                title=DATE_DIMENSION_TITLE_LOCALIZED,
                choices=list(self._get_date_dimension_values()),
            ),
            DimensionDTO(
                slug="category",
                title=CATEGORY_DIMENSION_TITLE_LOCALIZED,
                choices=[
                    DimensionValueDTO(
                        slug=category.slug,
                        title={self.language: category.title},
                        color=DEFAULT_COLORS.get(category.style, ""),
                    )
                    for category in Category.objects.filter(event=self.event)
                ],
            ),
            DimensionDTO(
                slug="tag",
                title=TAG_DIMENSION_TITLE_LOCALIZED,
                choices=[
                    DimensionValueDTO(slug=tag.slug, title={self.language: tag.title})
                    for tag in Tag.objects.filter(event=self.event)
                ],
            ),
            DimensionDTO(
                slug="room",
                title=ROOM_DIMENSION_TITLE_LOCALIZED,
                choices=[
                    DimensionValueDTO(slug=room.slug, title={self.language: room.name})
                    for room in Room.objects.filter(event=self.event)
                ],
            ),
        ]

    def get_program_dimension_values(self, programme: Programme) -> dict[str, str | list[str] | None]:
        return dict(
            date=self.get_date_dimension_value(programme),
            category=programme.category.slug,
            tag=[tag.slug for tag in programme.tags.all()],
            room=programme.room.slug if programme.room else None,
        )

    def get_length(self, programme: Programme) -> timedelta:
        """
        Return the length of the programme in minutes.
        """
        if not programme.length:
            raise ValueError(f"Programme {programme} has no length")

        return timedelta(minutes=programme.length)

    def get_start_time(self, programme: Programme) -> datetime:
        """
        Return the start time of the programme.
        """
        if not programme.start_time:
            raise ValueError(f"Programme {programme} has no start time")

        return programme.start_time

    def get_end_time(self, programme: Programme) -> datetime:
        """
        Return the end time of the programme.
        """
        return self.get_start_time(programme) + self.get_length(programme)

    program_unique_fields = ("event", "slug")
    program_update_fields = ("title", "description", "other_fields")

    def get_program(self, programme: Programme) -> Program:
        """
        Return an unsaved V2 Program instance for the V1 Programme.
        NOTE: If you add other fields not listed here, remember to add them to `program_update_fields`.
        """
        return Program(
            event=programme.category.event,
            slug=programme.slug,
            title=programme.title,
            description=programme.description,
            other_fields=dict(
                formatted_hosts=programme.formatted_hosts,
                signup_link=programme.signup_link,
            ),
        )

    def get_schedule_items(self, v1_programme: Programme, v2_program) -> list[ScheduleItem]:
        """
        Return a list of unsaved V2 ScheduleItems for the V1 Programme.
        """
        return [
            ScheduleItem(
                program=v2_program,
                start_time=self.get_start_time(v1_programme),
                length=self.get_length(v1_programme),
                # bulk create does not execute handlers, so we need to set this manually
                cached_end_time=self.get_end_time(v1_programme),
            )
        ]

    def import_program(self, queryset: QuerySet[Programme]):
        dimensions = self.get_dimensions()
        DimensionDTO.save_many(self.event, dimensions)
        logger.info("Imported %d dimensions for %s", len(dimensions), self.event.slug)

        v1_programmes = [programme for programme in queryset.order_by("id") if programme.state in PROGRAMME_STATES_LIVE]

        program_upsert = [self.get_program(programme) for programme in v1_programmes]
        v2_programs = Program.objects.bulk_create(
            program_upsert,
            update_conflicts=True,
            unique_fields=self.program_unique_fields,
            update_fields=self.program_update_fields,
        )
        logger.info("Imported %d programs for %s", len(v2_programs), self.event.slug)

        # cannot use ScheduleItem.objects.bulk_create(…, update_conflicts=True)
        # because there is no unique constraint
        ScheduleItem.objects.filter(program__in=v2_programs).delete()
        schedule_upsert = [
            schedule_item
            for v1_programme, v2_program in zip(v1_programmes, v2_programs, strict=True)
            for schedule_item in self.get_schedule_items(v1_programme, v2_program)
            if v1_programme.start_time is not None and v1_programme.length is not None
        ]
        schedule_items = ScheduleItem.objects.bulk_create(schedule_upsert)
        logger.info("Imported %d schedule items for %s", len(schedule_items), self.event.slug)

        upsert_cache = ProgramDimensionValue.build_upsert_cache(self.event)
        pdv_upsert = [
            item
            for programme, program_v2 in zip(v1_programmes, v2_programs, strict=True)
            for item in ProgramDimensionValue.build_upsertables(
                program_v2,
                self.get_program_dimension_values(programme),
                *upsert_cache,
            )
        ]
        pdvs = ProgramDimensionValue.bulk_upsert(pdv_upsert)
        logger.info("Imported %d program dimension values for %s", len(pdvs), self.event.slug)

        # delete program dimension values that are not set in the new data
        pdv_ids = {pdv.id for pdv in pdvs}
        ProgramDimensionValue.objects.filter(program__in=v2_programs).exclude(id__in=pdv_ids).delete()

        Program.refresh_cached_fields_qs(self.event.programs.all())

        return v2_programs
