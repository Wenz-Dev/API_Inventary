from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATA_BASE_URL = "sqlite:///./inventary.db"

engine = create_engine(
    DATA_BASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Generador de sesion para FastAPI"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()