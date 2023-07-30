import sqlite3 as sq

with sq.connect("my_db.db") as con:
    cur = con.cursor()

    cur.execute("""DROP TABLE IF EXISTS games""")
    cur.execute("""DROP TABLE IF EXISTS users""")

    cur.execute("""CREATE TABLE IF NOT EXISTS games(
    user_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    TIME INTEGER NOT NULL)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    row_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL,
    age INTEGER NOT NULL,
    score INTEGER)""")

    cur.execute("""INSERT INTO games VALUES(1, 200, 100000)""")
    cur.execute("""INSERT INTO games VALUES(1, 300, 110010)""")
    cur.execute("""INSERT INTO games VALUES(2, 500, 100010)""")
    cur.execute("""INSERT INTO games VALUES(1, 400, 201034)""")
    cur.execute("""INSERT INTO games VALUES(3, 100, 200010)""")
    cur.execute("""INSERT INTO games VALUES(2, 600, 210000)""")
    cur.execute("""INSERT INTO games VALUES(2, 300, 210010)""")

    cur.execute("""INSERT INTO users VALUES(1, 'Михаил', 1, 22, 1000)""")
    cur.execute("""INSERT INTO users VALUES(2, 'Яна', 2, 24, 830)""")
    cur.execute("""INSERT INTO users VALUES(3, 'Федор', 1, 32, 764)""")

    # сводная таблица из двух других
    res = cur.execute("SELECT name, sex, games.score FROM games JOIN users ON games.user_id = users.row_id")
    print(res.fetchall())
    # LEFT JOIN -- оператор работающий как JOIN, но если он не находит соответствие по условию в ресурсной талице,
    # то не пропускает эти поля, а в неизвестных данных указывает значение NULL

    # создание сводной таблицы 
    res = cur.execute("""SELECT name, sex, sum(games.score) as score FROM games JOIN users 
    ON games.user_id = users.row_id GROUP BY user_id ORDER BY score DESC""")

    print(res.fetchall())
