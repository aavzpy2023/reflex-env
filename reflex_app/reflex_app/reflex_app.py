import reflex as rx
from .pages.home import home_page
from .pages.login import login_page
from .state.auth_state import AuthState

# CORRECCIÓN DEFINITIVA: Se elimina el argumento `state=AuthState`.
# La versión actual de Reflex detecta las clases de estado automáticamente.
# Esta es la única línea que causa el traceback.
app = rx.App()

# Añadir las páginas y definir las rutas
app.add_page(login_page, route="/")
app.add_page(home_page, route="/home", on_load=AuthState.check_login_status)