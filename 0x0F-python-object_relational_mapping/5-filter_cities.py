#!/usr/bin/python3
"""Lists all cities of a state given as argument"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                LEFT JOIN states
                ON states.id = cities.state_id
                WHERE states.name=%s
                ORDER BY cities.id ASC""", (argv[4],))
    rows = cur.fetchall()
    print(", ".join([city for row in rows for city in row]))
