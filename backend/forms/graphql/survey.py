import graphene
from django.conf import settings
from graphene.types.generic import GenericScalar

from access.cbac import graphql_query_cbac_required
from core.graphql.common import DimensionFilterInput
from core.utils import normalize_whitespace

from ..models.form import Form
from ..models.survey import Survey
from .dimension import SurveyDimensionType
from .form import FormType
from .limited_survey import LimitedSurveyType
from .response import FullResponseType, LimitedResponseType

DEFAULT_LANGUAGE: str = settings.LANGUAGE_CODE


class SurveyType(LimitedSurveyType):
    @staticmethod
    def resolve_form(
        parent: Survey,
        info,
        lang: str = DEFAULT_LANGUAGE,
    ) -> Form | None:
        """
        Will attempt to give the form in the requested language, falling back
        to another language if that language is not available.
        """
        return parent.get_form(lang)

    form = graphene.Field(
        FormType,
        lang=graphene.String(),
        description=normalize_whitespace(resolve_form.__doc__ or ""),
    )

    @staticmethod
    def resolve_fields(
        parent: Survey,
        info,
        lang: str = DEFAULT_LANGUAGE,
        key_fields_only: bool = False,
    ):
        """
        A survey's language versions may have differing fields. This field presents
        them combined as a single list of fields. If a language is specified,
        that language is used as the base for the combined fields. Order of fields
        not present in the base language is not guaranteed.
        """
        fields = parent.get_combined_fields(lang)

        if key_fields_only:
            fields = (field for field in fields if field.slug in parent.key_fields)

        return [
            field.model_dump(
                exclude_none=True,
                by_alias=True,
            )
            for field in fields
        ]

    fields = graphene.Field(
        GenericScalar,
        lang=graphene.String(),
        key_fields_only=graphene.Boolean(),
        description=normalize_whitespace(resolve_fields.__doc__ or ""),
    )

    @graphql_query_cbac_required
    @staticmethod
    def resolve_responses(
        survey: Survey,
        info,
        filters: list[DimensionFilterInput] | None = None,
    ):
        """
        Returns the responses to this survey regardless of language version used.
        Authorization required.
        """
        if filters is None:
            filters = []

        queryset = survey.responses.all()

        for filter in filters:
            queryset = queryset.filter(
                dimensions__dimension__slug=filter.dimension,
                dimensions__value__slug__in=filter.values,
            )

        return queryset

    responses = graphene.List(
        graphene.NonNull(LimitedResponseType),
        filters=graphene.List(DimensionFilterInput),
        description=normalize_whitespace(resolve_responses.__doc__ or ""),
    )

    @graphql_query_cbac_required
    @staticmethod
    def resolve_response(survey: Survey, info, id: str):
        """
        Returns a single response to this survey regardless of language version used.
        Authorization required.
        """
        return survey.responses.filter(id=id).first()

    response = graphene.Field(
        FullResponseType,
        id=graphene.String(required=True),
    )

    @staticmethod
    def resolve_count_responses_by_current_user(survey: Survey, info):
        """
        Returns the number of responses to this survey by the current user.
        """
        if not info.context.user.is_authenticated:
            return 0

        return survey.responses.filter(created_by=info.context.user).count()

    count_responses_by_current_user = graphene.Field(
        graphene.NonNull(graphene.Int),
        description=normalize_whitespace(resolve_count_responses_by_current_user.__doc__ or ""),
    )

    @graphql_query_cbac_required
    @staticmethod
    def resolve_count_responses(survey: Survey, info):
        """
        Returns the number of responses to this survey regardless of language version used.
        Authorization required.
        """
        return survey.responses.count()

    count_responses = graphene.Field(
        graphene.NonNull(graphene.Int),
        description=normalize_whitespace(resolve_count_responses.__doc__ or ""),
    )

    @graphql_query_cbac_required
    @staticmethod
    def resolve_summary(survey: Survey, info, lang: str = DEFAULT_LANGUAGE):
        """
        Returns a summary of responses to this survey.  If a language is specified,
        that language is used as the base for the combined fields. Order of fields
        not present in the base language is not guaranteed. Authorization required.
        """
        return {slug: summary.model_dump(by_alias=True) for slug, summary in survey.get_summary(lang).items()}

    summary = graphene.Field(
        GenericScalar,
        lang=graphene.String(),
        description=normalize_whitespace(resolve_summary.__doc__ or ""),
    )

    @staticmethod
    def resolve_dimensions(survey: Survey, info, key_dimensions_only: bool = False):
        qs = survey.dimensions.all()

        if key_dimensions_only:
            qs = qs.filter(is_key_dimension=True)

        return qs

    dimensions = graphene.List(
        graphene.NonNull(SurveyDimensionType),
        key_dimensions_only=graphene.Boolean(),
    )

    class Meta:
        model = Survey
        fields = (
            "slug",
            "active_from",
            "active_until",
            "languages",
            "key_fields",
            "login_required",
            "anonymity",
            "max_responses_per_user",
        )
