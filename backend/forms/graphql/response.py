import graphene
from django.contrib.auth.models import User
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType

from core.graphql.user import LimitedUserType
from core.utils.text_utils import normalize_whitespace
from graphql_api.utils import resolve_local_datetime_field

from ..models.response import Response
from .dimension import ResponseDimensionValueType
from .form import FormType


class LimitedResponseType(DjangoObjectType):
    @staticmethod
    def resolve_values(
        response: Response,
        info,
        key_fields_only: bool = False,
    ):
        fields = response.form.validated_fields

        if key_fields_only:
            survey = response.form.survey
            key_fields = survey.key_fields if survey else []
            fields = [field for field in fields if field.slug in key_fields]

        # TODO discards warnings :(
        return response.get_processed_form_data(fields)[0]

    values = graphene.Field(
        GenericScalar,
        key_fields_only=graphene.Boolean(
            description=(
                "If the response is related to a survey, only return values of fields "
                "marked key fields in the survey. Note that setting keyFieldsOnly for a "
                "response not related to a survey will result in an empty dict."
            ),
        ),
    )

    @staticmethod
    def resolve_language(response: Response, info):
        return response.form.language

    language = graphene.Field(
        graphene.NonNull(graphene.String),
        description="Language code of the form used to submit this response.",
    )

    @staticmethod
    def resolve_created_by(response: Response, info) -> User | None:
        """
        Returns the user who submitted the response. If response is to an anonymous survey,
        this information will not be available.
        """
        if (survey := response.form.survey) and survey.anonymity in ("hard", "soft"):
            return None

        return response.created_by

    created_by = graphene.Field(
        LimitedUserType,
        description=resolve_created_by.__doc__,
    )

    @staticmethod
    def resolve_cached_dimensions(response: Response, info, key_dimensions_only: bool = False):
        """
        Returns the dimensions of the response as
        a dict of dimension slug -> list of dimension value slugs. If the response
        is not related to a survey, there will be no dimensions and an empty dict
        will always be returned.

        Using this field is more efficient than querying the dimensions field
        on the response, as the dimensions are cached on the response object.
        """
        cached_dimensions = response.cached_dimensions

        if key_dimensions_only:
            key_dimension_slugs = response.dimensions.filter(
                value__dimension__slug__in=cached_dimensions.keys(),
                value__dimension__is_key_dimension=True,
            ).values_list("value__dimension__slug", flat=True)

            return {k: v for k, v in cached_dimensions.items() if k in key_dimension_slugs}

        return cached_dimensions

    cached_dimensions = graphene.Field(
        GenericScalar,
        description=normalize_whitespace(resolve_cached_dimensions.__doc__ or ""),
        key_dimensions_only=graphene.Boolean(),
    )

    resolve_created_at = resolve_local_datetime_field("created_at")

    class Meta:
        model = Response
        fields = (
            "id",
            "form_data",
            "created_at",
            "sequence_number",
        )


class FullResponseType(LimitedResponseType):
    @staticmethod
    def resolve_form(parent: Response, info):
        return parent.form

    form = graphene.Field(graphene.NonNull(FormType))

    @staticmethod
    def resolve_dimensions(parent: Response, info, key_dimensions_only: bool = False):
        qs = parent.dimensions.all()

        if key_dimensions_only:
            qs = qs.filter(dimension__is_key_dimension=True)

        return qs

    dimensions = graphene.List(
        graphene.NonNull(ResponseDimensionValueType),
        key_dimensions_only=graphene.Boolean(),
    )

    class Meta:
        model = Response
        fields = (
            "id",
            "form_data",
            "created_at",
            "sequence_number",
        )


class ProfileResponseType(LimitedResponseType):
    @staticmethod
    def resolve_form(parent: Response, info):
        return parent.form

    form = graphene.Field(graphene.NonNull(FormType))

    @staticmethod
    def resolve_dimensions(response: Response, info, key_dimensions_only: bool = False):
        """
        The respondent will only see values of dimensions that are designated as
        being shown to the respondent.
        """
        qs = response.dimensions.filter(value__dimension__is_shown_to_subject=True)

        if key_dimensions_only:
            qs = qs.filter(value__dimension__is_key_dimension=True)

        return qs

    dimensions = graphene.List(
        graphene.NonNull(ResponseDimensionValueType),
        key_dimensions_only=graphene.Boolean(),
    )

    @staticmethod
    def resolve_cached_dimensions(response: Response, info, key_dimensions_only: bool = False):
        """
        Returns the dimensions of the response as
        a dict of dimension slug -> list of dimension value slugs. If the response
        is not related to a survey, there will be no dimensions and an empty dict
        will always be returned.

        Using this field is more efficient than querying the dimensions field
        on the response, as the dimensions are cached on the response object.

        The respondent will only see values of dimensions that are designated as
        being shown to the respondent.
        """
        cached_dimensions = response.cached_dimensions

        included_dimensions = response.dimensions.filter(
            value__dimension__slug__in=cached_dimensions.keys(),
            value__dimension__is_shown_to_subject=True,
        )

        if key_dimensions_only:
            included_dimensions = included_dimensions.filter(value__dimension__is_key_dimension=True)

        included_dimension_slugs = response.dimensions.values_list("value__dimension__slug", flat=True)

        return {k: v for k, v in cached_dimensions.items() if k in included_dimension_slugs}

    cached_dimensions = graphene.Field(
        GenericScalar,
        description=normalize_whitespace(resolve_cached_dimensions.__doc__ or ""),
        key_dimensions_only=graphene.Boolean(),
    )

    class Meta:
        model = Response
        fields = (
            "id",
            "form_data",
            "created_at",
        )
