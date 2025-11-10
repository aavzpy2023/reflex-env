import reflex as rx
import sqlmodel

from ..config.database import get_session
from ..models.schemas import User


class AuthState(rx.State):
    """Estado para gestionar la autenticación del usuario."""

    username: str = ""
    password: str = ""
    error_message: str = ""
    is_logged_in: bool = False

    def login(self):
        """Maneja el evento de inicio de sesión."""
        if not self.username or not self.password:
            self.error_message = "Usuario y contraseña son requeridos."
            return

        with next(get_session()) as session:
            user = session.exec(
                sqlmodel.select(User).where(User.username == self.username)
            ).first()

            # ADVERTENCIA: Comparación de texto plano. Usar hashing en producción.
            if user and user.password_hash == self.password:
                self.error_message = ""
                self.is_logged_in = True
                return rx.redirect("/home")
            else:
                self.error_message = "Credenciales inválidas."
                self.is_logged_in = False

    def logout(self):
        """Maneja el evento de cierre de sesión."""
        self.reset()
        return rx.redirect("/")

    def check_login_status(self):
        """Verifica si el usuario está logueado, redirige si no lo está."""
        if not self.is_logged_in:
            return rx.redirect("/")
