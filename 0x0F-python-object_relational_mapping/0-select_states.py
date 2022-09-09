#!/usr/bin/python3
"""Lists all states from database"""
import MySQLdb


def listStates(username, pass, dbse):
    """Lists all states from the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=pass, db=dbse)
    cur = db.cursor()
    cur.execute("SELECT %s, %s FROM dbse ORDER BY dbse.id", (id, name))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    listStates()
