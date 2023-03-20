#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

if __name__ == "__main__":
    db = MySQLdb.connect(username=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
