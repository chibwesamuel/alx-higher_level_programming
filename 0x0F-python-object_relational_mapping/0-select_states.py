#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(username=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id")
    [print(state) for state in c.fetchall()]