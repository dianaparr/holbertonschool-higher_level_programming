#!/usr/bin/python3
"""
Module of python called model_city_fetch_by_state
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def main():
    """ prints all City objects from the database hbtn_0e_14_usa

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

    # Querying data
    queryDB = session.query(State, City).filter(
                            State.id == City.state_id).order_by(City.id).all()
    for row in queryDB:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))

    session.close()

if __name__ == "__main__":
    main()
