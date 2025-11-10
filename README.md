# Plantilla de Proyecto de Reflex + Docker

Esta es una plantilla robusta y escalable para desarrollar aplicaciones web con [Reflex](https://reflex.dev/), totalmente contenerizada con Docker y optimizada para un flujo de trabajo de desarrollo profesional usando VS Code Dev Containers.

## 🎯 Características Principales

- **Fullstack en Python**: Frontend y backend con un único lenguaje.
- **Entorno Contenerizado**: Configuración con Docker y Docker Compose para desarrollo y testing.
- **Desarrollo Remoto**: Optimizado para GitHub Codespaces y VS Code Dev Containers.
- **Extensiones Pre-instaladas**: La imagen Docker incluye las extensiones de VS Code para una experiencia lista para usar, incluso sin conexión.
- **Testing Profesional**: Entorno de testing aislado con `pytest`.
- **Automatización**: `Makefile` con comandos para simplificar las operaciones comunes.
- **Configuración por Entorno**: Gestión de la configuración para desarrollo y testing a través de ficheros `.env`.
- **Arquitectura Modular**: Estructura de ficheros organizada por funcionalidad.

## 🚀 Inicio Rápido

### Prerrequisitos

- Docker y Docker Compose
- Visual Studio Code con la extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Pasos

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd reflex-app
    ```

2.  **Crear fichero `.env`:**
    No es necesario crear este fichero manualmente si no desea sobreescribir los valores por defecto. La configuración base se cargará automáticamente.

3.  **Abrir en Dev Container:**
    - Abra el proyecto en VS Code.
    - Presione `F1` y seleccione `Dev Containers: Reopen in Container`.
    - VS Code construirá la imagen Docker (la primera vez puede tardar) e iniciará el entorno.

### ✅ Verificación del Entorno

Una vez que el contenedor esté en funcionamiento (puede tomar 30-60 segundos después de que se abra la ventana de VS Code), verifique que la aplicación está corriendo:

1.  **Abra su navegador web.**
2.  **Navegue a [http://localhost](http://localhost).**
3.  **Deberá ver una página de bienvenida** con el título "Software Synergy Solutions" que confirma que todos los servicios del stack están operativos.

## 🛠️ Uso del `Makefile`

El `Makefile` proporciona un conjunto de comandos para gestionar el ciclo de vida del proyecto.

- `make up`: Inicia todos los servicios.
- `make down`: Detiene todos los servicios.
- `make build`: Reconstruye las imágenes Docker.
- `make logs`: Muestra los logs de la aplicación.
- `make shell`: Accede a una terminal dentro del contenedor de la aplicación.
- `make test`: Ejecuta la suite de tests.
- `make clean`: Limpia completamente el entorno Docker (contenedores, volúmenes, redes).
- `make init-db`: Ejecuta el script para crear las tablas en la base de datos.