#!/usr/bin/python
"""
Module of python called 5-filter_cities
"""
import MySQLdb
from sys import argv


def main():
    """ Takes in the name of a state as an argument and lists all cities
        of that state, using the database hbtn_0e_4_usa

        Connecting, creating and read a MySQL DB - methods:
            connect(parameters...) -> Use constructor for creating
                                      a connection to the DB that take
                                      3 arguments of the command line:
                                      [1]: username, [2]: password and
                                      [3]: DB name , [4]: state name searched.
            cursor() -> The MySQLCursor class instantiates objects that can
                        execute operations such as SQL statements
            execute() -> Executes the given database operation
                         (query or command) {SQL injection free!}
            fetchall() -> It fetches all the rows in a result set
    """
    # Data base connection
    connectDB = MySQLdb.connect(host="localhost", user=argv[1],
                                passwd=argv[2], db=argv[3],
                                port=3306, charset="utf8")
    # Query to DB using execute method of the created cursor
    cursor = connectDB.cursor()
    # The name must be matches the argument
    inputSearch = argv[4]
    queryDB = "SELECT cities.id, cities.name, states.name \
               FROM cities \
               INNER JOIN states \
               ON cities.state_id = states.id \
               WHERE states.name=%s \
               ORDER BY cities.id ASC"
    cursor.execute(queryDB, (inputSearch,))
    # Read operation
    listAll = cursor.fetchall()
    sep = ", "
    empty = ""
    for row in listAll:
        values = [row[1]]
        print(empty, end="")
        print(values[0], end="")
        empty = sep
    print("")
    # Closing the connection
    connectDB.close()

if __name__ == '__main__':
    main()
