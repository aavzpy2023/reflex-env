FROM nginx:1.25-alpine

# Eliminar configuración por defecto para evitar conflictos
RUN rm /etc/nginx/conf.d/default.conf

# Copiar nuestra configuración personalizada
COPY nginx.conf /etc/nginx/conf.d/default.conf