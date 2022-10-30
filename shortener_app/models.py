"""Defines how data should be stored in the db."""


from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class URL(Base):
    __tablename__="urls"

    id = Column(Integer, primary_key=True)
    # Random string that will be part of the shortened URL
    key = Column(String, unique=True, index=True)
    # To manage the shortened URL and see statistics
    secret_key = Column(String, unique=True, index=True)
    # URL for which we generate short urls
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
