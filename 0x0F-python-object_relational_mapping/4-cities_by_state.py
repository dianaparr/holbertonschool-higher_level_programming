#!/usr/bin/python3
"""
Module of python called 4-cities_by_state
"""
import MySQLdb
from sys import argv


def main():
    """ Lists all cities from the database hbtn_0e_4_usa

        Connecting, creating and read a MySQL DB - methods:
            connect(parameters...) -> Use constructor for creating
                                      a connection to the DB that take
                                      3 arguments of the command line:
                                      [1]: username, [2]: password and
                                      [3]: DB name.
            cursor() -> The MySQLCursor class instantiates objects that can
                        execute operations such as SQL statements
            execute() -> Executes the given database operation
                         (query or command)
            fetchall() -> It fetches all the rows in a result set
    """
    # Data base connection
    connectDB = MySQLdb.connect(host="localhost", user=argv[1],
                                passwd=argv[2], db=argv[3],
                                port=3306, charset="utf8")
    # Query to DB using execute method of the created cursor
    cursor = connectDB.cursor()
    queryDB = "SELECT cities.id, cities.name, states.name \
               FROM cities \
               INNER JOIN states \
               ON cities.state_id = states.id \
               ORDER BY cities.id ASC"
    cursor.execute(queryDB)
    # Read operation
    listAll = cursor.fetchall()
    for row in listAll:
        print(row)
    # Closing the connection
    connectDB.close()

if __name__ == '__main__':
    main()
