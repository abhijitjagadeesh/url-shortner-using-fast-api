"""Contains info about DB connection."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

# creates a db engine an entrypoint to the db
engine = create_engine(
    get_settings().db_url,
    # enables more than one request at a time to communicate with the the sqlite db
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# a base class to connect the db engine to sqlalchemy functionality of models
Base = declarative_base()
