from typing import Tuple

import reflex as rx
from reflex.components.radix.themes.layout.stack import HStack


def services() -> rx.Component:
    return rx.box(
        rx.heading("OUR SERVICES", align="center", as_="h2", width="100%"),
        rx.flex(
            rx.flex(
                rx.heading("TATTOO", as_="h2", align="center"),
                rx.text("SERVICE", align="center"),
                rx.center(
                    rx.button("See Artists")
                ),
                background="center/cover url('/tattoo.jpg')",
                width="50%",
                direction="column"
            ),
            rx.flex(  # Mudei rx.heading para rx.vstack para centralizar verticalmente o texto.
                rx.heading("PIERCINGS", as_="h2", align="center"),  # Adicionei align="center" para centralizar o texto.
                rx.text("SERVICE", align="center"),
                rx.center(
                    rx.button("See Artists")
                ),
                background="center/cover url('/tattoo.jpg')",
                width="50%",
                direction="column"
            ),
            width="100%",
        )
    )
