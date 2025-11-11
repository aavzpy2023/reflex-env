# Entorno de Desarrollo Profesional para Aplicaciones Reflex

## 1. Resumen Ejecutivo

Este repositorio contiene un entorno de desarrollo "todo en uno", robusto y completamente contenerizado, diseñado para la creación de aplicaciones web full-stack con el framework [Reflex](https://reflex.dev/).

La filosofía detrás de esta plantilla es la **reproducibilidad total y la experiencia de desarrollador de grado militar**. El entorno está pre-configurado con todas las herramientas, extensiones de VS Code y servicios necesarios para comenzar a desarrollar de inmediato, eliminando la necesidad de instalar dependencias en la máquina local. Está optimizado para ser utilizado con **GitHub Codespaces** y **VS Code Dev Containers**.

## 2. Pila Tecnológica

Este entorno de desarrollo integra los siguientes componentes con versiones fijadas para garantizar la estabilidad:

| Componente      | Versión          | Propósito                                       |
| --------------- | ---------------- | ----------------------------------------------- |
| **Framework**   | `Reflex`         | `0.8.18`         | Desarrollo Full-Stack en Python                 |
| **Lenguaje**      | `Python`         | `3.13`           | Lógica de la aplicación                         |
| **Base de Datos** | `PostgreSQL`     | `16`             | Almacenamiento de datos relacional              |
| **Proxy Inverso** | `Nginx`          | `1.25`           | Enrutamiento de tráfico al frontend/backend     |
| **Orquestación**  | `Docker Compose` | `v2+`            | Definición y gestión del entorno multi-contenedor |
| **Seguridad**     | `passlib`        | `1.7.4`          | Hashing de contraseñas (con backend `bcrypt`)   |

## 3. Guía de Inicio Rápido

### Prerrequisitos

*   [Docker](https://www.docker.com/products/docker-desktop/) y Docker Compose
*   [Visual Studio Code](https://code.visualstudio.com/)
*   Extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) para VS Code

### Pasos de Configuración

1.  **Clonar el Repositorio**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2.  **Crear el Archivo de Entorno (`.env`)**
    Cree un archivo llamado `.env` en la raíz del proyecto. **Este paso es mandatorio.** Puede copiar el siguiente template:
    ```dotenv
    # General
    ENVIRONMENT=development
    DEBUG=True
    LOG_LEVEL=DEBUG
    SECRET_KEY=super-secret-dev-key

    # PostgreSQL
    POSTGRES_DB=app_db_dev
    POSTGRES_USER=app_user
    POSTGRES_PASSWORD=app_password
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432

    # Reflex App
    REFLEX_DB_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
    REFLEX_FRONTEND_PORT=3000
    REFLEX_BACKEND_PORT=8000

    # Nginx
    NGINX_PORT=80
    ```

3.  **Lanzar el Dev Container**
    *   Abra el proyecto en VS Code.
    *   Abra la paleta de comandos (`Ctrl+Shift+P` o `Cmd+Shift+P`).
    *   Seleccione y ejecute **"Dev Containers: Reopen in Container"**.
    *   La primera vez, la construcción de la imagen puede tardar varios minutos. Las ejecuciones posteriores serán casi instantáneas.

### Verificación del Entorno

Una vez que el contenedor esté en funcionamiento, todos los servicios se iniciarán automáticamente.
*   **Acceda a la aplicación:** Abra su navegador y navegue a `http://localhost`.
*   **Verá la página de inicio de sesión.**

## 4. Flujo de Trabajo de Desarrollo

### Acceder a la Shell del Contenedor

Para ejecutar comandos dentro del contenedor de la aplicación (ej. scripts, migraciones), utilice la terminal integrada de VS Code. Ya estará dentro del contenedor. Alternativamente, desde su máquina local:

```bash
docker exec -it reflex_app bash