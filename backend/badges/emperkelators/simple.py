from typing import Self

import pydantic

from badges.utils import default_badge_factory
from core.models.event import Event
from core.models.person import Person
from labour.models.personnel_class import PersonnelClass


class SimpleEmperkelator(pydantic.BaseModel):
    """
    Assumes perks are recorded in PersonnelClass.override_formatted_perks
    and gives the perks of the personnel class indicated by the default badge factory.
    No stacking of perks is done.
    """

    override_formatted_perks: str = ""

    def __str__(self):
        return self.override_formatted_perks

    @classmethod
    def emperkelate(
        cls,
        event: Event,
        person: Person,
    ) -> Self:
        badge_opts = default_badge_factory(event, person)
        personnel_class: PersonnelClass | None = badge_opts.get("personnel_class")  # type: ignore

        if not personnel_class:
            return cls(override_formatted_perks="")

        return cls(override_formatted_perks=personnel_class.override_formatted_perks)
