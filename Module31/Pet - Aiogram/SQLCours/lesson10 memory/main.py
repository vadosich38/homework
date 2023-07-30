import sqlite3 as sq

data = [('car', 'машина'), ('house', 'дом'), ('tree', 'дерево'), ('color', 'цвет')]

con = sq.connect(":memory:")
with con:
    cur = con.cursor()

    cur.executescript("""
    DROP TABLE IF EXISTS dict;
    
    CREATE TABLE IF NOT EXISTS dict(
    eng TEXT,
    rus TEXT)""")

    cur.executemany("INSERT INTO dict VALUES(?, ?)", data)

    res = cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(res.fetchall())
