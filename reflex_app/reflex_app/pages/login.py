import reflex as rx

from ..state.auth_state import AuthState


def login_page() -> rx.Component:
    """La página de inicio de sesión."""
    return rx.center(
        rx.vstack(
            rx.heading("Iniciar Sesión", size="8"),
            rx.input(placeholder="Usuario", on_blur=AuthState.set_username, size="3"),
            rx.input(
                placeholder="Contraseña",
                type="password",
                on_blur=AuthState.set_password,
                size="3",
            ),
            rx.button("Entrar", on_click=AuthState.login, size="3"),
            rx.cond(
                AuthState.error_message != "",
                rx.text(AuthState.error_message, color="red", margin_top="1em"),
            ),
            spacing="4",
            align="center",
        ),
        height="100vh",
    )
