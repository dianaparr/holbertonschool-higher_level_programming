#!/usr/bin/python3
"""
Module of python called relationship_city
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State

# returns a new base class from which all mapped classes should inherit
Base = declarative_base()


class City(Base):
    """ Defining a class called City that has three properties:

            - The __tablename__ property tells SQLAlchemy that rows
              of the cities table must be mapped to this class.
            - The id property identifies that this is the primary_key
              in the table and that its type is Integer.
            - The name property indicates that a column in the table has
              the name of the property and that its type is String.
            - Class attribute state_id that represents a column of an integer,
              can't be null and is a foreign key to states.id.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    relToState = relationship("State", cascade="save-update")
