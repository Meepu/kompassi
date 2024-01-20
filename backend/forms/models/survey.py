from __future__ import annotations

from collections.abc import Collection, Mapping
from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Event
from core.utils import NONUNIQUE_SLUG_FIELD_PARAMS, is_within_period

from ..utils.merge_form_fields import merge_fields
from .form import Form

if TYPE_CHECKING:
    from .dimension import Dimension, DimensionValue

DEFAULT_LANGUAGE: str = settings.LANGUAGE_CODE
ANONYMITY_CHOICES = [
    # not linked to user account, IP address not recorded
    ("hard", _("Hard anonymous")),
    # linked to user account but not shown to owner, IP address recorded
    ("soft", _("Soft anonymous (linked to user account but not shown to survey owner)")),
    # linked to user account and shown to owner, IP address recorded
    ("name_and_email", _("Name and email shown to survey owner if responded logged-in")),
]


class Survey(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="surveys")
    slug = models.CharField(**NONUNIQUE_SLUG_FIELD_PARAMS)  # type: ignore

    login_required = models.BooleanField(
        default=False,
        verbose_name=_("Login required"),
    )

    max_responses_per_user = models.PositiveIntegerField(
        default=0,
        verbose_name=_("max responses per user"),
        help_text=_(
            "Maximum number of responses per user. 0 = unlimited. "
            "Note that if login_required is not set, this only takes effect for logged in users."
            "Has no effect if the survey is hard anonymous."
        ),
    )

    anonymity = models.CharField(
        max_length=max(len(key) for key, _ in ANONYMITY_CHOICES),
        choices=ANONYMITY_CHOICES,
        default="soft",
        verbose_name=_("anonymity"),
        help_text=_(
            "Hard anonymous: responses are not linked to user accounts and IP addresses are not recorded. "
            "Soft anonymous: responses are linked to user accounts but not shown to survey owners. "
            "Name and email: responses are linked to user accounts and shown to survey owners."
        ),
    )

    active_from = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("active from"),
        help_text=_(
            "The form will be available from this date onwards. " "If not set, the form will not be available."
        ),
    )

    active_until = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("active until"),
        help_text=_(
            "The form will be available until this date. "
            "If not set, the form will be available indefinitely "
            "provided that active_from is set and has passed."
        ),
    )

    languages = models.ManyToManyField(
        "forms.Form",
        verbose_name=_("language versions"),
        help_text=_(
            "The form will be available in these languages. "
            "Each language can have its own set of fields. "
            "There must be exactly one form per supported language."
        ),
    )

    key_fields = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        default=list,
        verbose_name=_("key fields"),
        help_text=_("Key fields will be shown in the response list."),
    )

    # related fields
    dimensions: models.QuerySet[Dimension]

    @property
    def is_active(self):
        return is_within_period(self.active_from, self.active_until)

    def admin_is_active(self):
        return self.is_active

    admin_is_active.short_description = _("active")
    admin_is_active.boolean = True

    @property
    def combined_fields(self):
        return self.get_combined_fields()

    def get_combined_fields(self, base_language: str = DEFAULT_LANGUAGE):
        """
        See ../graphql.py:SurveyType.resolve_combined_fields
        for documentation.
        """
        # TODO as an optimization, store boolean field in survey model that indicates
        # whether the fields are the same across languages. If so, return the fields
        # from the base language directly.

        # if a specific language is requested, put it first
        languages = sorted(
            self.languages.all().only("language", "fields"),
            key=lambda form: form.language != base_language,
        )

        return merge_fields(languages)

    def get_form(self, requested_language: str) -> Form | None:
        try:
            return self.languages.get(language=requested_language)
        except Form.DoesNotExist:
            pass

        for language, _name in settings.LANGUAGES:
            if language == requested_language:
                # already tried above, skip one extra query
                continue

            try:
                return self.languages.get(language=language)
            except Form.DoesNotExist:
                pass

        raise Form.DoesNotExist()

    @property
    def responses(self):
        from .response import Response

        return Response.objects.filter(form__in=self.languages.all()).order_by("created_at")

    def get_summary(self, base_language: str = DEFAULT_LANGUAGE):
        from ..utils.summarize_responses import summarize_responses

        fields = self.get_combined_fields(base_language)
        valuesies = [response.get_processed_form_data(fields)[0] for response in self.responses.all().only("form_data")]

        return summarize_responses(fields, valuesies)

    def preload_dimensions(self, dimension_values: Mapping[str, Collection[str]] | None = None):
        dimensions = self.dimensions.all().prefetch_related("values")
        if dimension_values is not None:
            dimensions = dimensions.filter(slug__in=dimension_values.keys())

        dimensions_by_slug = {dimension.slug: dimension for dimension in dimensions}

        values_by_dimension_by_slug: dict[str, dict[str, DimensionValue]] = {}
        for dimension in dimensions_by_slug.values():
            values_by_dimension_by_slug[dimension.slug] = {value.slug: value for value in dimension.values.all()}

        return dimensions_by_slug, values_by_dimension_by_slug

    class Meta:
        unique_together = [("event", "slug")]

    def __str__(self):
        return f"{self.event.slug}/{self.slug}"
