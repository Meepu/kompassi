from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from .views import (
    enrollment_enroll_view,
    enrollment_admin_view,
    enrollment_admin_special_diets_view,
)

urlpatterns = [
    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/enrollment/(?P<enrollment_slug>[a-z0-9-]+)/?$',
        enrollment_enroll_view,
        name='enrollment_enroll_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/enrollment/(?P<enrollment_slug>[a-z0-9-]+)/admin/?$',
        enrollment_admin_view,
        name='enrollment_admin_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/enrollment/(?P<enrollment_slug>[a-z0-9-]+)/admin/specialdiets/?$',
        enrollment_admin_special_diets_view,
        name='enrollment_admin_special_diets_view'
    ),
]
