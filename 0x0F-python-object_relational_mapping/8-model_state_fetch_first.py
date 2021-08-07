#!/usr/bin/python3
"""
Module of python called model_state_fetch_first
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def main():
    """ Prints the first State object from the database hbtn_0e_6_usa

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
    queryDB = session.query(State).first()
    if queryDB is None:
        print("Nothing")
    else:
        print("{}: {}".format(queryDB.id, queryDB.name))

    session.close()

if __name__ == "__main__":
    main()
