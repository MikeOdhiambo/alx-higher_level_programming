#!/usr/bin/python3
"""Lists all values where the names match the argument"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE states.name=%s
                ORDER BY states.id ASC""", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
