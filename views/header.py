import reflex as rx
from components.navbar import navbar


def header() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.heading("WELCOME TO", as_="h2"),
            rx.heading("ATLANTIC", as_="h1"),
            rx.heading("TATTOO STUDIO", as_="h2"),
            rx.hstack(
                rx.button(
                    "TATTOOS",
                ),
                rx.button(
                    "PIERCING",
                )
            ),
            direction="column"
        )
    )
