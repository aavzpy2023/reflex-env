
    
FROM python:3.13-slim-bookworm

# ------------------------------------------------------------------------------------
# CONFIGURACIÓN DEL ENTORNO BASE Y DE LA APLICACIÓN
# ------------------------------------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# ------------------------------------------------------------------------------------
# INSTALACIÓN DE DEPENDENCIAS DEL SISTEMA
# ------------------------------------------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential curl libpq-dev git unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------------------------------
# INSTALACIÓN DEL VS CODE SERVER (ENFOQUE ROBUSTO)
# ------------------------------------------------------------------------------------
ARG INSTALL_DIR="/root/.vscode-server"
RUN mkdir -p "${INSTALL_DIR}"

# CORRECCIÓN CRÍTICA: Descargar dinámicamente el VS Code Server en lugar de copiarlo.
# Esto hace que el build sea auto-contenido y reproducible.
RUN curl -L "https://update.code.visualstudio.com/latest/server-linux-x64/stable" -o /tmp/vscode-server.tar.gz && \
    tar -xzf /tmp/vscode-server.tar.gz -C "${INSTALL_DIR}" --strip-components 1 && \
    rm /tmp/vscode-server.tar.gz

# ------------------------------------------------------------------------------------
# INSTALACIÓN DE EXTENSIONES DE VS CODE
# ------------------------------------------------------------------------------------
# Recrear el alias 'code' esperado por los scripts de instalación de extensiones.
RUN ln -s "${INSTALL_DIR}/bin/code-server" "${INSTALL_DIR}/bin/code"
ENV PATH="${INSTALL_DIR}/bin:${PATH}"

# Define las extensiones a instalar usando sus IDs oficiales
ARG VSCODE_EXTENSIONS="ms-python.python ms-python.vscode-pylance charliermarsh.ruff ms-python.black-formatter eamodio.gitlens ms-azuretools.vscode-docker rangav.vscode-thunder-client ckolkman.vscode-postgres mtxr.sqltools littlefoxteam.vscode-python-test-adapter ms-vscode.test-adapter-converter ms-vscode.makefile-tools github.copilot ms-vscode.vscode-file-utils christian-kohler.path-intellense usernamehw.errorlens"

# Itera e instala cada extensión.
RUN for ext in ${VSCODE_EXTENSIONS}; do \
        code --install-extension ${ext} --force; \
    done

# ------------------------------------------------------------------------------------
# INSTALACIÓN DE DEPENDENCIAS DE PYTHON
# ------------------------------------------------------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .