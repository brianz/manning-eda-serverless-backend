from typing import Tuple
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader([
        "src/notifications/templates",
        "notifications/templates",
        "templates",
    ]),
    autoescape=select_autoescape(),
)


def render_new_order(event_detail: dict) -> Tuple[str, str]:
    html_template = env.get_template("order-email.html.j2")
    txt_template = env.get_template("order-email.txt.j2")

    return (
        txt_template.render(**event_detail),
        html_template.render(**event_detail),
    )
