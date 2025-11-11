# --- ETAPA 1: La Fábrica Autónoma de Cache (Builder) ---
# Esta etapa sigue una secuencia causal estricta para garantizar un build reproducible.
FROM python:3.13-slim-bookworm as builder

WORKDIR /app

# 1. Instalar dependencias del sistema y de JS.
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unzip nodejs npm && \
    apt-get clean
RUN npm install -g bun

# 2. Instalar dependencias de Python. Esto es necesario para tener el comando 'reflex'.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiar el código fuente de la aplicación.
COPY . .

# 4. EL PASO CRÍTICO: Ejecutar 'reflex init'.
# Esto genera el directorio '/app/.web' y el 'package.json' necesario.
RUN reflex init

# 5. POBLAR EL CACHE: Ahora que '/app/.web/package.json' existe,
# este comando tendrá éxito y poblará el cache de Bun.
RUN bun install --cwd .web

# --- ETAPA 2: La Imagen de Desarrollo Final ---
# Esta etapa es idéntica a la anterior, pero ahora hereda un cache válido.
FROM python:3.13-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential curl libpq-dev git unzip nodejs npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:${PATH}"

# Copiar el cache de Bun pre-poblado desde la etapa 'builder'.
COPY --from=builder /root/.bun /root/.bun

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

COPY . .
RUN pip install --no-cache-dir -r requirements.txt