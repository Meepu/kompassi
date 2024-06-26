import datetime
import re

import jinja2.nodes
from jinja2 import is_undefined, pass_eval_context
from jinja2.runtime import Undefined
from markupsafe import Markup

from .files import NameFactory

SValue = str | Undefined


def add_all_to(filters: dict[str, callable]) -> None:
    filters["nl2br"] = nl2br
    filters["filename"] = NameFactory.sanitize
    filters.update(make_date_fns())


@pass_eval_context
def nl2br(eval_ctx: jinja2.nodes.EvalContext, value: SValue, with_p: int = 0) -> Markup | SValue:
    if is_undefined(value):
        return value
    br = "<br>\n"

    if eval_ctx.autoescape:
        br = Markup(br)

    pl = ""
    pr = ""
    if with_p:
        pl = "<p>"
        pr = "</p>"

    result = "\n\n".join(f"{pl}{br.join(p.splitlines())}{pr}" for p in re.split(r"(?:\r\n|\r(?!\n)|\n){2,}", value))
    return Markup(result) if eval_ctx.autoescape else result


def make_date_fns(datetime_input: str | None = None, date_input: str | None = None) -> dict:
    datetime_input = datetime_input or "%Y-%m-%d %H:%M:%S"
    date_input = date_input or "%Y-%m-%d"

    def datetime_format(value: datetime.datetime | str | Undefined, format: str = "%H:%M %d-%m-%y") -> SValue:
        if is_undefined(value):
            return value
        if isinstance(value, str):
            value = datetime.datetime.strptime(value, datetime_input)
        return value.strftime(format)

    def date(value: datetime.date | str | Undefined) -> SValue:
        if is_undefined(value):
            return value
        if isinstance(value, str):
            value = datetime.datetime.strptime(value, date_input).date()
        return value

    def timedelta(value: datetime.datetime | Undefined, days: int) -> datetime.datetime | Undefined:
        if is_undefined(value):
            return value
        return value + datetime.timedelta(days=days)

    return {
        "datetime": datetime_format,
        "date": date,
        "timedelta": timedelta,
    }
