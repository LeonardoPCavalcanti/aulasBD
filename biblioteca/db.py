from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/biblioteca_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
