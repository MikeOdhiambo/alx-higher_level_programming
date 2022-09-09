#!/usr/bin/python3
"""0-select_states.py - Lists states"""


def listStates(username, pass, db_name):
    """Lists all the states in the database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=pass, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY db_name.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    import MySQLdb
    import sys
    listStates(sys.argv[1], sys.argv[2], sys.argv[3])
