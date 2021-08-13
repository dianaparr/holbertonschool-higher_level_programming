#!/usr/bin/python3
"""
Module of python called relationship_states_cities_list
"""
from sys import argv
from relationship_state import Base, State
import model_state
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def main():
    """ Lists all State objects, and corresponding City objects, contained
        in the database hbtn_0e_101_usa

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

    # # Querying data:
    list_queryDB = session.query(State).order_by(State.id)
    # print(list_queryDB)

    for elementState in list_queryDB:
        print("{}: {}".format(elementState.id, elementState.name))
        # print("{}-----state".format(elementState))
        for elementCity in elementState.cities:
            print("\t{}: {}".format(elementCity.id, elementCity.name))
            # print("{}----city".format(elementState.cities))

    # Write changes to the database
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
