#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """python3 -c 'print(__import__("my_module").__doc__)' """
    db = MySQLdb.connect(username=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id")
    [print(state) for state in c.fetchall()]
