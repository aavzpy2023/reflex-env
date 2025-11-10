
import reflex as rx
import sqlmodel
from ..config.database import get_session
from ..models.schemas import User
from ..core.security import verify_password

class AuthState(rx.State):
    """Estado para gestionar la autenticación del usuario."""
    username: str = ""
    password: str = ""
    error_message: str = ""
    is_logged_in: bool = False

    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.password = password

    def login(self):
        """Maneja el evento de inicio de sesión usando verificación de hash."""
        # --- INICIO DE INSTRUMENTACIÓN DE DIAGNÓSTICO ---
        print("--- [Evento de Login Iniciado] ---")
        print(f"Intento de login para usuario: '{self.username}'")

        if not self.username or not self.password:
            self.error_message = "Usuario y contraseña son requeridos."
            return
        
        with next(get_session()) as session:
            user = session.exec(
                sqlmodel.select(User).where(User.username == self.username)
            ).first()

            if user:
                print(f"Usuario '{user.username}' encontrado en la base de datos.")
                print(f"Hash almacenado: {user.password_hash}")
                
                # Verificación de la contraseña
                is_valid_password = verify_password(self.password, user.password_hash)
                print(f"Resultado de verify_password: {is_valid_password}")

                if is_valid_password:
                    print("¡Éxito! Redirigiendo a /home.")
                    self.error_message = ""
                    self.is_logged_in = True
                    return rx.redirect("/home")
            else:
                print(f"Usuario '{self.username}' NO encontrado en la base de datos.")

        # Si llegamos aquí, la autenticación falló
        print("Fallo de autenticación. Estableciendo mensaje de error.")
        self.error_message = "Credenciales inválidas."
        print("--- [Evento de Login Finalizado con Fallo] ---")
        # --- FIN DE INSTRUMENTACIÓN DE DIAGNÓSTICO ---

    def logout(self):
        self.reset()
        return rx.redirect("/")

    def check_login_status(self):
        if not self.is_logged_in:
            return rx.redirect("/")