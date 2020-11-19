from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os


DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
POSTGRES_URL = os.getenv("POSTGRES_URL", "localhost:5432/")
DATABASE_URI = f"postgres://{DB_USER}:{DB_PASSWORD}@{POSTGRES_URL}"

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
