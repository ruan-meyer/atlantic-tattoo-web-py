import reflex as rx
from components.navbar import navbar
from styles.constants import Size as Size


def header() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.heading("WELCOME TO", as_="h2", font_size=Size.BIG),
            rx.heading("ATLANTIC", as_="h1", font_size=Size.VERY_BIG, margin_y=Size.VERY_SMALL),
            rx.heading("TATTOO STUDIO", as_="h1", font_size=Size.BIG, margin_bottom=Size.VERY_SMALL),
            rx.hstack(
                rx.button(
                    "TATTOOS",
                ),
                rx.button(
                    "PIERCING",
                )
            ),
            direction="column",
            margin_y=Size.BIG,
        )
    )
