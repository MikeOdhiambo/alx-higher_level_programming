#!/usr/bin/python3
"""Defines a State class"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from the Base declarative class
    Attributes:
        __tablename__: link to MySQL table
        id: id column to map
        name: name column to map
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
