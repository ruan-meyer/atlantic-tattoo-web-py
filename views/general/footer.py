import reflex as rx


def footer() -> rx.Component:
    return rx.flex(
        rx.center(
            rx.image("favicon.ico")
        ),
        rx.box(
            rx.text("Atlantic Tattoo", align="center"),
            rx.text("Calle Amalia Alayon, 3. Los Cristianos, Tenerife", align="center"),
            rx.text("Copyright © 2024. Powered by rmeyer.dev", align="center")
        ),
        direction="column"
    )
