import reflex as rx
from styles.constants import Color as Color


BASE_STYLE = {
    rx.button: {
        "background_color": Color.SECONDARY,
        "color": Color.DARK,
        "border_radius": "100px",
        ":hover": {
            "background_color": Color.DARK,
            "color": Color.SECONDARY,
        }
    },
    rx.link: {

    }
}
