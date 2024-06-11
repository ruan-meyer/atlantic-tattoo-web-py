import reflex as rx
from components.artist import artist


def artists() -> rx.Component:
    return rx.box(
        rx.heading("OUR ARTISTS", as_="h2", align="center", width="100%"),
        rx.flex(
            artist(name="ARTIST", artist_type="Tattoo artist", image_name="tattoo.jpg"),
            artist(name="ARTIST", artist_type="Tattoo artist", image_name="tattoo.jpg"),
            artist(name="ARTIST", artist_type="Tattoo artist", image_name="tattoo.jpg"),
            spacing="3"
        ),
    )
