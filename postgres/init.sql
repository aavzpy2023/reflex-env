-- Este script se ejecuta automáticamente al crear la base de datos por primera vez.
-- Puede usarse para crear roles, esquemas o extensiones.

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Nota: Las tablas son creadas por SQLAlchemy a través del script init_db.py
-- por lo que no es necesario definirlas aquí.