#!/usr/bin/python3
"""
Module of python called 0-select states
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Data base connection
    connectDB = MySQLdb.connect(host="localhost", user=argv[1],
                                passwd=argv[2], db=argv[3],
                                port=3306)
    # Query to DB using execute method of the created cursor
    cursor = connectDB.cursor()
    queryDB = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(queryDB)
    # Read operation
    listAll = cursor.fetchall()
    for row in listAll:
        print(row)
    # Closing the connection
    connectDB.close()
