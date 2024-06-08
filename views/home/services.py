import reflex as rx


def services() -> rx.Component:
    return rx.box(
        rx.heading("OUR SERVICES", as_="h2", align="center"),
        rx.hstack(
            rx.center(
                rx.vstack(
                    rx.heading("TATTOO", as_="h2", align="center"),
                    rx.text("SERVICE"),
                    rx.button("See Artists"),
                ),
                background="center/cover url('/tattoo.jpg')",
                width="50%",
                height="100%",
            ),
            rx.center(
                rx.heading("PIERCINGS", as_="h2"),
                rx.text("SERVICE"),
                rx.button("See Artists"),
                background="center/cover url('/tattoo.jpg')",
                width="50%",
                height="100%",
            )
        )
    )
