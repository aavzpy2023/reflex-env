CREATE TABLE IF NOT EXISTS "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO "user" (username, password_hash)
SELECT 'admin', '$2b$12$BWw/LP0qdRhF8O8TmTB9OeOxTkjTYBlZYH/kcEBZRb82GCbS.f7fG' 
WHERE NOT EXISTS (
    SELECT 1 FROM "user" WHERE username = 'admin'
);