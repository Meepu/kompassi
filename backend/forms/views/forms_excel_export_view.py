from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

from access.cbac import default_cbac_required
from core.models import Event

from ..excel_export import write_responses_as_excel
from ..models.dimension import Dimension
from ..models.form import Form


@default_cbac_required
def forms_excel_export_view(
    request: HttpRequest,
    event_slug: str | None,
    form_slug: str,
):
    timestamp = now().strftime("%Y%m%d%H%M%S")

    if event_slug:
        event = get_object_or_404(Event, slug=event_slug)
        form = get_object_or_404(Form, event=event, slug=form_slug)
        filename = f"{event.slug}_{form.slug}_responses_{timestamp}.xlsx"
    else:
        form = get_object_or_404(Form, event__isnull=True, slug=form_slug)
        filename = f"{form.slug}_responses_{timestamp}.xlsx"

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    write_responses_as_excel(
        Dimension.objects.none(),
        form.validated_fields,
        form.responses.all().only("form_data"),
        response,
    )

    return response
