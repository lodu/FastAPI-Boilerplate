from src.database import Base, engine, models, SessionLocal, schemas
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


fake_user_1 = {
    "email": "fastapi@fastapi.fastapi",
    "password": "fastapiPASS",
    "full_name": "fastapi ipatsaf",
    "disabled": False,
    "username": "apiFAST",
}

fake_user_2 = {
    "email": "fastapi@boiler.plate",
    "password": "boilerPASS",
    "full_name": "boiler reliob",
    "disabled": True,
    "username": "plateBOILER",
}


def create_fake_data():
    insert_params = f"{tuple(fake_user_1.values())}, {tuple(fake_user_2.values())}"
    query = f"INSERT INTO users (email, hashed_password, full_name, disabled, username) VALUES {insert_params}"
    with engine.connect() as conn:
        res = conn.execute(query)


def make_fake_db():
    recreate_database()
    create_fake_data()
