from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
import os

engine = create_engine("sqlite+pysqlite:///./data/qa_agent.db")
Session = sessionmaker(bind=engine)


def init_db():
    """Initialize the database tables if they don't exist"""
    db_path = "./data/qa_agent.db"
    db_exists = os.path.exists(db_path)

    Base.metadata.create_all(engine)

    if not db_exists:
        print("Database created for the first time")
    else:
        print("Using existing database")


def get_db():
    session = Session()
    return session
