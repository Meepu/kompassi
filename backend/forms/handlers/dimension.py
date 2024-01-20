from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.forms import ValidationError

from core.utils import slugify

from ..models.dimension import Dimension, DimensionValue, ResponseDimensionValue
from ..models.response import Response


@receiver(pre_save, sender=ResponseDimensionValue)
def program_dimension_value_pre_save(sender, instance: ResponseDimensionValue, **kwargs):
    if instance.dimension is None:
        instance.dimension = instance.value.dimension
    elif instance.dimension != instance.value.dimension:
        raise ValidationError({"dimension": "Dimension value does not belong to the dimension"})


@receiver([post_save, post_delete], sender=Dimension)
@receiver([post_save, post_delete], sender=DimensionValue)
def dimension_post_save(sender, instance: Dimension | DimensionValue, **kwargs):
    Response.refresh_cached_dimensions(instance.survey.responses.all())


@receiver([post_save, post_delete], sender=ResponseDimensionValue)
def response_dimension_value_post_save(sender, instance: ResponseDimensionValue, **kwargs):
    response = instance.response
    response.cached_dimensions = response.build_cached_dimensions()
    response.save(update_fields=["cached_dimensions"])


@receiver(pre_save, sender=(Dimension, DimensionValue))
def dimension_pre_save(sender, instance: Dimension | DimensionValue, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title.en or instance.title.fi)
