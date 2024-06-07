"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from views.header import header


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.container(
        header(),
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


app = rx.App()
app.add_page(index)
