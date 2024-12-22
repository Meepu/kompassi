import graphene

from access.cbac import graphql_check_instance
from core.models.event import Event

from ...models.order import Order
from ...optimized_server.models.enums import RefundType
from ..order_limited import LimitedOrderType


class RefundOrderInput(graphene.InputObjectType):
    event_slug = graphene.String(required=True)
    order_id = graphene.String(required=True)
    refund_type = graphene.InputField(graphene.Enum.from_enum(RefundType), required=True)


class RefundOrder(graphene.Mutation):
    class Arguments:
        input = RefundOrderInput(required=True)

    order = graphene.Field(LimitedOrderType)

    @staticmethod
    def mutate(
        root,
        info,
        input: RefundOrderInput,
    ):
        event = Event.objects.get(slug=input.event_slug)
        order = Order.objects.get(event=event, id=input.order_id)
        refund_type = RefundType(input.refund_type)
        graphql_check_instance(order, info, "self", "update")
        order.refund(refund_type)
        return RefundOrder(order=order)  # type: ignore
