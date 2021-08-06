#!/usr/bin/python
"""
Module of python called 3-my_safe_filter_states
"""
import MySQLdb
from sys import argv


def main():
    """ Takes in an argument and displays all values in the states table
        of hbtn_0e_0_usa where name matches the argument, that is safe from
        MySQL injections.

        Connecting, creating and read a MySQL DB - methods:
            connect(parameters...) -> Use constructor for creating
                                      a connection to the DB that take
                                      4 arguments of the command line:
                                      [1]: username, [2]: password and
                                      [3]: DB name, [4]: state name searched.
            cursor() -> The MySQLCursor class instantiates objects that can
                        execute operations such as SQL statements
            execute() -> Executes the given database operation
                         (query or command). Must use format to create the SQL
                         query with the user input.
            fetchall() -> It fetches all the rows in a result set
    """
    # Data base connection
    connectDB = MySQLdb.connect(host="localhost", user=argv[1],
                                passwd=argv[2], db=argv[3],
                                port=3306, charset="utf8", )
    # Query to DB using execute method of the created cursor
    cursor = connectDB.cursor()
    # The name must be matches the argument
    inputSearch = argv[4]
    # Query safe for oyu to execute, is passed as a named parameter
    queryDB = "SELECT * FROM states WHERE name=%s \
                ORDER BY id ASC"
    cursor.execute(queryDB, (inputSearch,))
    # Read operation
    listAll = cursor.fetchall()
    for row in listAll:
        print(row)
    # Closing the connection
    connectDB.close()

if __name__ == '__main__':
    main()
