import sqlmodel
from rxconfig import config

DATABASE_URL = config.db_url

if not DATABASE_URL:
    raise ValueError(
        "Database URL not configured. Ensure REFLEX_DB_URL is set in your .env file."
    )

engine = sqlmodel.create_engine(DATABASE_URL)

def get_session():
    with sqlmodel.Session(engine) as session:
        yield session