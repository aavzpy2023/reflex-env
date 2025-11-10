.PHONY: help build up down restart logs shell clean test init-db

# Variables
APP_CONTAINER_NAME=app
TEST_COMPOSE_FILE=docker-compose.test.yml

help:
	@echo "✅ SSS - Project Command Interface"
	@echo "-------------------------------------"
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  up           - 🚀 Inicia todos los servicios en segundo plano (dev)."
	@echo "  down         - 🛑 Detiene y elimina los contenedores."
	@echo "  restart      - 🔄 Reinicia los servicios."
	@echo "  build        - 🛠️ Construye o reconstruye las imágenes Docker."
	@echo "  logs         - 📜 Muestra los logs en tiempo real para la app."
	@echo "  shell        - 💻 Accede a un shell (bash) dentro del contenedor de la app."
	@echo "  clean        - 🧹 Elimina contenedores, redes y volúmenes (¡CUIDADO!)."
	@echo "  test         - 🧪 Ejecuta la suite de tests en un entorno aislado."
	@echo "  init-db      - 💾 Ejecuta el script de inicialización de la base de datos."


ps:
	@echo "Listando contenedores..."
	docker-compose ps

up:
	@echo "🚀 Iniciando entorno de desarrollo..."
	docker-compose up -d

down:
	@echo "🛑 Deteniendo entorno..."
	docker-compose down

restart: down up

build:
	@echo "🛠️ Construyendo imágenes..."
	docker-compose up -d --build

logs:
	@echo "📜 Siguiendo logs de la aplicación..."
	docker-compose logs -f $(APP_CONTAINER_NAME)

shell:
	@echo "💻 Accediendo al contenedor de la aplicación..."
	docker-compose exec $(APP_CONTAINER_NAME) bash

clean:
	@echo "🧹 Limpiando el entorno Docker por completo..."
	docker-compose down -v --remove-orphans
	docker system prune -af

test:
	@echo "🧪 Ejecutando tests..."
	docker-compose -f $(TEST_COMPOSE_FILE) up --build --abort-on-container-exit

init-db:
	@echo "💾 Inicializando la base de datos..."
	docker-compose exec $(APP_CONTAINER_NAME) python scripts/init_db.py