#!/usr/bin/python3
"""
Module of python called relationship_states_cities
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def main():
    """ Creates the State “California” with the City “San Francisco” from the
        database hbtn_0e_100_usa

        The basic functionality of SQLAlchemy, which is the SQL expression
        language, is used, to create some metadata that will contain a series
        of modules (or objects).

            1 Create a DB engine to establish connection, which takes 3 command
               line arguments: [1]: username, [2]: password and [3]: DB name.
            2 Use the .create_all() method on the metadata object and pass it
              the engine connection for SQLAlchemy to generate a table.
            3 Create a session to interact with the DB. I create an access
              to the Session custom class and I create an instance
              of it (without argument).
            4 Query the DB using the query() method of the session object.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Sessionmaker class with creates Session class with default arguments
    # set for its constructor.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add new data and send to DB
    newDataState = State(name="California")
    # Add state in this city
    newDataCity = City(name="San Francisco", state=newDataState)

    session.add(newDataState)
    session.add(newDataCity)
    session.commit()

    session.close()

if __name__ == "__main__":
    main()
