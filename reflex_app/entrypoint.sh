
# Iniciar el backend de Reflex (Uvicorn) en segundo plano
echo "Iniciando el backend de Reflex..."
cd /app/backend
uvicorn reflex_app.reflex_app:app --host 0.0.0.0 --port 8000 &

# Iniciar un servidor web simple para el frontend estático en segundo plano
echo "Iniciando el servidor de frontend estático..."
cd /app/frontend
python -m http.server 3000 &

# Esperar a que cualquier proceso termine y salir.
# Esto mantiene el contenedor en ejecución.
wait -n