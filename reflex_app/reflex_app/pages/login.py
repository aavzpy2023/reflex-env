import reflex as rx
from ..state.auth_state import AuthState

def login_page() -> rx.Component:
    """La página de inicio de sesión."""
    return rx.center(
        rx.form(
            rx.vstack(
                rx.heading("Iniciar Sesión", size="8"),
                rx.input(
                    placeholder="Usuario",
                    on_change=AuthState.set_username,
                    size="3",
                    width="210%"
                ),
                rx.input(
                    placeholder="Contraseña",
                    type="password",
                    on_change=AuthState.set_password,
                    size="3",
                    width="20%"
                ),
                rx.button("Entrar", type="submit", size="3", width="100%"),
                rx.cond(
                    AuthState.error_message != "",
                    rx.text(AuthState.error_message, color="red", margin_top="1em")
                ),
                spacing="4",
                align="center",
            ),
            on_submit=AuthState.login,
        ),
        height="100vh",
    )