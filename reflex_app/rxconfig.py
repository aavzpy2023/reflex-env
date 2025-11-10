import reflex as rx


config = rx.Config(
    app_name="reflex_app",
    
    db_url=None,

    frontend_port=3000,
    backend_port=8000,

    # REFUERZO: Se añade el host del backend aquí para que la configuración
    # sea explícita y centralizada, alineándose con el comando de Docker.
    backend_host="0.0.0.0",
    state_auto_setters=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
    ],
)