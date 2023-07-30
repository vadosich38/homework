import sqlite3 as sq

with sq.connect("my_db.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS tab1")
    cur.execute("DROP TABLE IF EXISTS tab2")

    cur.execute("""CREATE TABLE IF NOT EXISTS tab1(
    score INTEGER NOT NULL,
    `from` TEXT NOT NULL)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tab2(
    val INTEGER NOT NULL,
    type TEXT NOT NULL)""")

    cur.execute("INSERT INTO tab1 VALUES(100, 'tab1')")
    cur.execute("INSERT INTO tab1 VALUES(200, 'tab1')")
    cur.execute("INSERT INTO tab1 VALUES(300, 'tab1')")

    cur.execute("INSERT INTO tab2 VALUES(200, 'tab2')")
    cur.execute("INSERT INTO tab2 VALUES(300, 'tab2')")
    cur.execute("INSERT INTO tab2 VALUES(400, 'tab2')")

    # объединение двух таблиц через JOIN
    res = cur.execute("SELECT score, `from` FROM tab1 UNION SELECT val, type FROM tab2")
    print(res.fetchall())

    # объединение двух таблиц через JOIN с постоянным занчением второго столбца
    res = cur.execute("SELECT score, 'Таблица 1' as source FROM tab1 UNION SELECT val, 'Таблица 2' FROM tab2")
    print(res.fetchall())

    # тоже самое с фильтром, лимитом, сортировкой
    res = cur.execute("""
    SELECT score, 'Таблица 1' as source FROM tab1 WHERE score IN(300, 400) 
    UNION SELECT val, 'Таблица 2' FROM tab2
    ORDER BY score DESC
    LIMIT 3""")

    print(res.fetchall())
