import graphene

from core.graphql.event_full import FullEventType
from core.graphql.mutations.confirm_email import ConfirmEmail
from core.graphql.profile import ProfileType
from core.models import Event, Person
from forms.graphql.mutations.create_survey import CreateSurvey
from forms.graphql.mutations.create_survey_language import CreateSurveyLanguage
from forms.graphql.mutations.create_survey_response import CreateSurveyResponse
from forms.graphql.mutations.delete_survey import DeleteSurvey
from forms.graphql.mutations.delete_survey_dimension import DeleteSurveyDimension
from forms.graphql.mutations.delete_survey_dimension_value import DeleteSurveyDimensionValue
from forms.graphql.mutations.delete_survey_language import DeleteSurveyLanguage
from forms.graphql.mutations.delete_survey_responses import DeleteSurveyResponses
from forms.graphql.mutations.generate_key_pair import GenerateKeyPair
from forms.graphql.mutations.init_file_upload import InitFileUpload
from forms.graphql.mutations.put_survey_dimension import PutSurveyDimension
from forms.graphql.mutations.put_survey_dimension_value import PutSurveyDimensionValue
from forms.graphql.mutations.revoke_key_pair import RevokeKeyPair
from forms.graphql.mutations.subscriptions import SubscribeToSurveyResponses, UnsubscribeFromSurveyResponses
from forms.graphql.mutations.update_form import UpdateForm
from forms.graphql.mutations.update_form_fields import UpdateFormFields
from forms.graphql.mutations.update_response_dimensions import UpdateResponseDimensions
from forms.graphql.mutations.update_survey import UpdateSurvey
from program_v2.graphql.mutations.favorites import (
    MarkProgramAsFavorite,
    MarkScheduleItemAsFavorite,
    UnmarkProgramAsFavorite,
    UnmarkScheduleItemAsFavorite,
)
from program_v2.graphql.mutations.feedback import CreateProgramFeedback
from tickets_v2.graphql.mutations.cancel_and_refund_order import CancelAndRefundOrder
from tickets_v2.graphql.mutations.create_product import CreateProduct
from tickets_v2.graphql.mutations.create_quota import CreateQuota
from tickets_v2.graphql.mutations.delete_product import DeleteProduct
from tickets_v2.graphql.mutations.delete_quota import DeleteQuota
from tickets_v2.graphql.mutations.reorder_products import ReorderProducts
from tickets_v2.graphql.mutations.resend_order_confirmation import ResendOrderConfirmation
from tickets_v2.graphql.mutations.update_order import UpdateOrder
from tickets_v2.graphql.mutations.update_product import UpdateProduct
from tickets_v2.graphql.mutations.update_quota import UpdateQuota

from .language import DEFAULT_LANGUAGE, Language


class LanguageType(graphene.ObjectType):
    code = graphene.String()
    name = graphene.String(lang=graphene.String())

    @staticmethod
    def resolve_name(
        language: Language,
        info,
        lang: str = DEFAULT_LANGUAGE,
    ):
        if lang == "fi":
            return language.name_fi
        else:
            return language.name_en


class Query(graphene.ObjectType):
    @staticmethod
    def resolve_event(root, info, slug: str):
        return Event.objects.filter(slug=slug).first()

    event = graphene.Field(FullEventType, slug=graphene.String(required=True))

    @staticmethod
    def resolve_profile(root, info):
        if not info.context.user.is_authenticated:
            return None

        try:
            return info.context.user.person
        except Person.DoesNotExist:
            return None

    profile = graphene.Field(ProfileType)


class Mutation(graphene.ObjectType):
    # Core
    confirm_email = ConfirmEmail.Field()

    # Forms
    create_survey = CreateSurvey.Field()
    update_survey = UpdateSurvey.Field()
    delete_survey = DeleteSurvey.Field()

    create_survey_language = CreateSurveyLanguage.Field()
    update_form = UpdateForm.Field()
    update_form_fields = UpdateFormFields.Field()
    delete_survey_language = DeleteSurveyLanguage.Field()

    create_survey_response = CreateSurveyResponse.Field()
    update_response_dimensions = UpdateResponseDimensions.Field()
    delete_survey_responses = DeleteSurveyResponses.Field()

    put_survey_dimension = PutSurveyDimension.Field()
    delete_survey_dimension = DeleteSurveyDimension.Field()

    put_survey_dimension_value = PutSurveyDimensionValue.Field()
    delete_survey_dimension_value = DeleteSurveyDimensionValue.Field()

    init_file_upload = InitFileUpload.Field()

    generate_key_pair = GenerateKeyPair.Field()
    revoke_key_pair = RevokeKeyPair.Field()

    # Program v2
    mark_program_as_favorite = MarkProgramAsFavorite.Field()
    unmark_program_as_favorite = UnmarkProgramAsFavorite.Field()
    mark_schedule_item_as_favorite = MarkScheduleItemAsFavorite.Field()
    unmark_schedule_item_as_favorite = UnmarkScheduleItemAsFavorite.Field()

    create_program_feedback = CreateProgramFeedback.Field()

    subscribe_to_survey_responses = SubscribeToSurveyResponses.Field()
    unsubscribe_from_survey_responses = UnsubscribeFromSurveyResponses.Field()

    # Tickets v2
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    reorder_products = ReorderProducts.Field()

    create_quota = CreateQuota.Field()
    update_quota = UpdateQuota.Field()
    delete_quota = DeleteQuota.Field()

    update_order = UpdateOrder.Field()
    resend_order_confirmation = ResendOrderConfirmation.Field()
    cancel_and_refund_order = CancelAndRefundOrder.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
