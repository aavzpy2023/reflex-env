FROM python:3.13-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# ------------------------------------------------------------------------------------
# INSTALACIÓN DE DEPENDENCIAS DEL SISTEMA Y JAVASCRIPT RUNTIMES
# ------------------------------------------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential curl libpq-dev git unzip nodejs npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# --- PASO DE VERIFICACIÓN DE GRADO MILITAR (NPM) ---
RUN npm --version

# Instalar Bun
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:${PATH}"

# --- PASO DE VERIFICACIÓN DE GRADO MILITAR (BUN) ---
RUN bun --version

# ------------------------------------------------------------------------------------
# INSTALACIÓN DEL VS CODE SERVER Y EXTENSIONES
# ------------------------------------------------------------------------------------
ARG INSTALL_DIR="/root/.vscode-server"
RUN mkdir -p "${INSTALL_DIR}"
RUN curl -L "https://update.code.visualstudio.com/latest/server-linux-x64/stable" -o /tmp/vscode-server.tar.gz && \
    tar -xzf /tmp/vscode-server.tar.gz -C "${INSTALL_DIR}" --strip-components 1 && \
    rm /tmp/vscode-server.tar.gz
RUN ln -s "${INSTALL_DIR}/bin/code-server" "${INSTALL_DIR}/bin/code"
ENV PATH="${INSTALL_DIR}/bin:${PATH}"

ARG VSCODE_EXTENSIONS="ms-python.python ms-python.vscode-pylance charliermarsh.ruff ms-python.black-formatter eamodio.gitlens ms-azuretools.vscode-docker rangav.vscode-thunder-client ckolkman.vscode-postgres mtxr.sqltools littlefoxteam.vscode-python-test-adapter ms-vscode.test-adapter-converter ms-vscode.makefile-tools github.copilot ms-vscode.vscode-file-utils christian-kohler.path-intellense usernamehw.errorlens"
RUN for ext in ${VSCODE_EXTENSIONS}; do \
        code --install-extension ${ext} --force; \
    done

# ------------------------------------------------------------------------------------
# INSTALACIÓN DE CÓDIGO FUENTE Y DEPENDENCIAS DE PYTHON
# ------------------------------------------------------------------------------------
COPY . .
RUN pip install --no-cache-dir -r requirements.txt