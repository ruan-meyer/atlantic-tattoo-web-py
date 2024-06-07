import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.link("HOME")
        ),
        rx.vstack(
            rx.link("ABOUT")
        ),
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.text(
                        "SERVICES"
                    ),
                    rx.icon("chevron-down"),
                    variant="ghost"
                ),
            ),
            rx.menu.content(
                rx.menu.item("TATTOO"),
                rx.menu.item("PIERCING"),
                rx.menu.item("AFTER CARE"),
            ),
        ),
        rx.vstack(
            rx.link("CONTACT")
        )
    )
