#!/usr/bin/python
"""
Module of python called 1-filter_states
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Lists all states with a name starting with N (upper N)
        from the database hbtn_0e_0_usa

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
    queryDB = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(queryDB)
    # Read operation
    listAll = cursor.fetchall()
    for row in listAll:
        print(row)
    # Closing the connection
    connectDB.close()
