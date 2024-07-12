import reflex as rx


def about() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading("TITLE", as_="h1"),
            rx.text("text text text text text text text text text text text text text text text text text text text "
                    "text text text text text text text text text text text text text text text text text text text "
                    "text text text text text text text text text text text text text text text text text text text "
                    "text text text text text text text text text text text text text text text text text text text "
                    ),
            rx.button("Read More"),
            width="50%"
        ),
        rx.vstack(
            rx.image(src="tattoo.jpg"),
            width="50%"
        ),
        background_color="black"
    )
