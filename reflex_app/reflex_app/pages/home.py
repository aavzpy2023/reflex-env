import reflex as rx

from ..state.auth_state import AuthState


def home_page() -> rx.Component:
    """La página de bienvenida, visible solo para usuarios autenticados."""
    return rx.fragment(
        rx.cond(
            AuthState.is_logged_in,
            rx.center(
                rx.vstack(
                    rx.heading(f"Bienvenido, {AuthState.username}!", size="8"),
                    rx.button(
                        "Cerrar Sesión",
                        on_click=AuthState.logout,
                        margin_top="1em",
                        size="3",
                    ),
                    align="center",
                ),
                height="100vh",
            ),
        )
    )
