# encoding: utf-8

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import cache_page, cache_control
from django.views.decorators.http import require_safe

from api.utils import api_view
from core.tabs import Tab
from core.sort_and_filter import Filter
from core.utils import url

from ..models import (
    AllRoomsPseudoView,
    Category,
    Programme,
    View,
)
from ..helpers import (
    group_programmes_by_start_time,
    programme_event_required,
    public_programme_required,
)


def get_timetable_tabs(request, event):
    timetable_url = url('programme_timetable_view', event.slug)
    timetable_active = request.path == timetable_url
    timetable_text = 'Ohjelmakartta'

    special_url = url('programme_special_view', event.slug)
    special_active = request.path == special_url
    special_text = 'Ohjelmakartan ulkopuolinen ohjelma'

    return [
        Tab(timetable_url, timetable_text, timetable_active, 0),
        Tab(special_url, special_text, special_active, 0),
    ]


SCHEDULE_TEMPLATES = dict(
    reasonable='programme_timetable_view.jade',
    full_width='programme_full_width_timetable_view.jade',
)


@public_programme_required
@cache_control(public=True, max_age=5 * 60)
@cache_page(5 * 60)  # XXX remove once nginx cache is in place
@require_safe
def programme_timetable_view(
    request,
    event,
    internal_programmes=False,
    template=None,
    show_programme_actions=False,
):
    vars = dict(
        # hide the user menu to prevent it getting cached
        login_page=True,
        tabs=get_timetable_tabs(request, event),
    )

    return actual_timetable_view(request, event,
        internal_programmes=internal_programmes,
        template=template,
        vars=vars,
        show_programme_actions=show_programme_actions,
    )


# look, no cache
@programme_event_required
@require_safe
def programme_internal_timetable_view(
    request,
    event,
    internal_programmes=True,
    template=None,
):
    vars = dict(
        tabs=get_timetable_tabs(request, event),
    )

    return actual_timetable_view(request, event,
        internal_programmes=internal_programmes,
        template=template,
        vars=vars,
        show_programme_actions=True,
    )


def actual_timetable_view(
    request,
    event,
    internal_programmes=False,
    template=None,
    vars=None,
    show_programme_actions=False,
):
    if template is None:
        template = SCHEDULE_TEMPLATES[event.programme_event_meta.schedule_layout]

    if not vars:
        vars = dict()

    all_rooms = AllRoomsPseudoView(event)

    category_query = dict(event=event)

    if not internal_programmes:
        category_query.update(public=True)

    vars.update(
        event=event,
        views=View.objects.filter(event=event, public=True),
        categories=Category.objects.filter(**category_query),
        internal_programmes=internal_programmes,
        programmes_by_start_time=all_rooms.get_programmes_by_start_time(request=request),
        show_programme_actions=show_programme_actions,
    )

    return render(request, template, vars)


@public_programme_required
@require_safe
def programme_special_view(
    request,
    event,
    template='programme_special_view.jade',
    show_programme_actions=False,
):
    return actual_special_view(request, event,
        template=template,
        show_programme_actions=show_programme_actions,
    )


def actual_special_view(
    request,
    event,
    include_unpublished=False,
    template='programme_special_view.jade',
    vars=None,
    show_programme_actions=False,
):
    criteria = dict(include_unpublished=include_unpublished)

    category_slug = request.GET.get('category')
    if category_slug:
        criteria.update(category__slug=category_slug)

    programmes = event.programme_event_meta.get_special_programmes(**criteria).order_by('start_time')

    categories_criteria = dict(event=event)
    if not include_unpublished:
        categories_criteria.update(public=True)
    categories = Category.objects.filter(**categories_criteria)
    category_filters = Filter(request, 'category').add_objects('category__slug', categories)
    programmes = category_filters.filter_queryset(programmes)

    programmes_by_start_time = group_programmes_by_start_time(programmes)

    if vars is None:
        vars = dict()

    vars.update(
        category_filters=category_filters,
        event=event,
        programmes_by_start_time=programmes_by_start_time,
        show_programme_actions=show_programme_actions,
        tabs=get_timetable_tabs(request, event),
    )

    return render(request, template, vars)


@user_passes_test(lambda u: u.is_superuser)
@require_safe
def programme_internal_dumpdata_view(request):
    from django.core import management
    from io import StringIO

    buffer = StringIO()
    management.call_command('dumpdata', 'programme', stdout=buffer)
    response = HttpResponse(buffer.getvalue(), 'application/json')
    buffer.close()

    return response


@cache_control(public=True, max_age=1 * 60)
@cache_page(1 * 60)  # XXX remove once nginx cache is in place
@public_programme_required
@require_safe
def programme_mobile_timetable_view(request, event):
    vars = dict(event=event)

    return render(request, 'programme_mobile_timetable.jade', vars)


@programme_event_required
@require_safe
def programme_internal_adobe_taggedtext_view(request, event):
    vars = dict(programmes_by_start_time=AllRoomsPseudoView(event).get_programmes_by_start_time(request=request))
    data = render_to_string('programme_timetable.taggedtext', vars, request=request)

    # force all line endings to CRLF (Windows)
    data = data.replace('\r\n', '\n').replace('\n', '\r\n')

    # encode to UTF-16; the LE at the end means no BOM, which is absolutely critical
    data = data.encode('UTF-16LE')

    return HttpResponse(data, 'text/plain; charset=utf-16')


@programme_event_required
@require_safe
@api_view
def programme_json_view(request, event, format='default', include_unpublished=False):
    criteria = dict(category__event=event)

    if not include_unpublished:
        criteria.update(state='published')

    programmes = (
        Programme.objects.filter(**criteria)
            .select_related('category__event')
            .select_related('room')
            .prefetch_related('tags')

            # Does not do the needful due to formatted_organizers operating on the "through" model
            # .prefetch_related('organizers')
    )

    return [programme.as_json(format=format) for programme in programmes]


def programme_profile_menu_items(request):
    programme_url = url('programme_profile_view')
    programme_active = request.path.startswith(programme_url)
    programme_text = _('Programmes')

    return [
        (programme_active, programme_url, programme_text)
    ]


def programme_event_box_context(request, event):
    return dict(
        is_programme_admin=event.programme_event_meta.is_user_admin(request.user),
    )
