import reflex as rx
from styles.constants import Size as Size
from styles.constants import Color as Color


def service(service_type: str) -> rx.Component:
    return rx.flex(
        rx.heading(service_type, as_="h2", align="center", font_size=Size.BIG, color=Color.SECONDARY),
        rx.text("SERVICE", align="center", font_size=Size.LARGE, color=Color.DARK),
        rx.center(
            rx.button("See Artists", font_size=Size.DEFAULT)
        ),
        background="center/cover url('/tattoo.jpg')",
        width="50%",
        height="20em",
        direction="column",
        justify_content="center",
    )


def services() -> rx.Component:
    return rx.box(
        rx.heading("OUR SERVICES", align="center", as_="h2", width="100%"),
        rx.flex(
            service(service_type="TATTOO"),
            service(service_type="PIERCING"),
            width="100%",
        )
    )
