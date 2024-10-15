#!/usr/bin/env python3
"""
Defines a User model for SQLAlchemy with fields for user information.

Classes:
    User: A table representing users, including email, hashed password,
          session ID, and reset token.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """SQLAlchemy User model."""

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)
