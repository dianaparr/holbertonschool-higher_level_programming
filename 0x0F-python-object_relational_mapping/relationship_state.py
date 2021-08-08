#!/usr/bin/python3
"""
Module of python called relationship_state
Class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# returns a new base class from which all mapped classes should inherit
Base = declarative_base()


class State(Base):
    """ Defining a class called State that has three properties:

            - The __tablename__ property tells SQLAlchemy that rows
              of the states table must be mapped to this class.
            - The id property identifies that this is the primary_key
              in the table and that its type is Integer.
            - The name property indicates that a column in the table has
              the name of the property and that its type is String.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    # "The delete-orphan and all symbols indicates that the child object should
    # follow along with its parent in all cases, and be deleted once it is no
    # longer associated with that parent"
    relToCities = relationship("City", back_populates="state")
