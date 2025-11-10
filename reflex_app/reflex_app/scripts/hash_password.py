import sys
from reflex_app.core.security import get_password_hash

def main():
    if len(sys.argv) != 2:
        print("Uso: python -m scripts.hash_password 'su-contraseña-aqui'")
        sys.exit(1)
    
    password = sys.argv[1]
    hashed_password = get_password_hash(password)
    print("Contraseña en texto plano:", password)
    print("Hash generado (BCrypt):", hashed_password)

if __name__ == "__main__":
    main()