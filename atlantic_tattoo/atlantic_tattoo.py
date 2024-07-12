"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from views.home.header import header as home_header
from views.home.about import about as home_about
from views.home.services import services
from views.home.artists import artists
from views.general.footer import footer
import styles.styles


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        home_header(),
        home_about(),
        services(),
        artists(),
        footer()
    )


def about() -> rx.Component:
    pass


def tattoo() -> rx.Component:
    pass


def piercing() -> rx.Component:
    pass


def after_care() -> rx.Component:
    pass


def contact() -> rx.Component:
    pass


app = rx.App(
    style=styles.styles.BASE_STYLE
)
app.add_page(index)
