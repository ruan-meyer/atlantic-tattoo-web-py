import reflex as rx


def artist(name: str, artist_type: str, image_name: str) -> rx.Component:
    return rx.flex(
        rx.image(image_name),
        rx.heading(name, align="center"),
        rx.text(artist_type, align="center"),
        rx.center(
            rx.button("Portfolio")
        ),
        direction="column"
    )
