import sqlite3 as sq

with sq.connect(database="my_db.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    score INTEGER NOT NULL)
    """)

    #записать данные во все столбцы таблицы
    cur.execute("INSERT INTO users VALUES(1, 'Михаил', 19, 1, 1000)")
    cur.execute("INSERT INTO users VALUES(2, 'Alex', 10, 1, 3400)")
    cur.execute("INSERT INTO users VALUES(3, 'Illya', 29, 1, 3000)")
    cur.execute("INSERT INTO users VALUES(4, 'Kolya', 9, 1, 1200)")

    #записать данные в выбранные столбцы
    cur.execute("INSERT INTO users (name, age, score) VALUES('Иван', 25, 200)")
    cur.execute("INSERT INTO users (name, age, score) VALUES('Jora', 2, 700)")
    cur.execute("INSERT INTO users (name, age, score) VALUES('Oleg', 23, 400)")
    cur.execute("INSERT INTO users (name, age, score) VALUES('Petr', 12, 800)")

    #выбираем все полня из таблицы
    res = cur.execute("SELECT * FROM users")
    print("Все записи в таблице:", res.fetchall())

    # выбираем указаные полня из таблицы
    res = cur.execute("SELECT age, score FROM users")
    print("Возраст, очки:", res.fetchall())

    # выбираем все полня из таблицы, где число очков больше 1000
    res = cur.execute("SELECT * FROM users WHERE score > 1000")
    print("Все у кого очков больше 1000:", res.fetchall())

    # выбираем все полня из таблицы, где число очков между 500 и 2000
    res = cur.execute("SELECT * FROM users WHERE score BETWEEN 500 and 2000")
    print("Все у кого очков от 500 до 2000:", res.fetchall())

    # выбираем все полня из таблицы, где число очков равно 200
    res = cur.execute("SELECT * FROM users WHERE score == 200")
    print("Все у кого очков равно 200:", res.fetchall())

    # выбираем все полня из таблицы, где возраст от 15 и очков менее 1000
    res = cur.execute("SELECT * FROM users WHERE age > 15 and score < 1000")
    print("Все у кого возраст больше 15 и очков менее 1000:", res.fetchall())

    # выбираем все полня из таблицы, где возраст равен 25 или 23 и очков более 50
    res = cur.execute("SELECT * FROM users WHERE age IN(25, 23) and score > 50")
    print("Все у кого возраст 25 или 23 и очков более 50:", res.fetchall())

    # выбираем все полня из таблицы, где число очков между 500 и 2000 с сортировкой по возрасту
    res = cur.execute("SELECT * FROM users WHERE score BETWEEN 500 and 2000 ORDER BY age")
    print("Все у кого очков от 500 до 2000 с сортировкой по возрасту:", res.fetchall())

    # выбираем все полня из таблицы, где число очков между 500 и 2000 с сортировкой по возрасту явно
    res = cur.execute("SELECT * FROM users WHERE score BETWEEN 500 and 2000 ORDER BY age ASC")
    print("Все у кого очков от 500 до 2000 с сортировкой по возрасту явно:", res.fetchall())

    # выбираем все полня из таблицы, где число очков между 500 и 2000 с сортировкой по убыванию по возрасту
    res = cur.execute("SELECT * FROM users WHERE score BETWEEN 500 and 2000 ORDER BY age DESC")
    print("Все у кого очков от 500 до 2000 с сортировкой по убыванию по возрасту:", res.fetchall())

    # выбираем первые 3 поля из таблицы, где число очков между 500 и 2000
    res = cur.execute("SELECT * FROM users WHERE score BETWEEN 500 and 2000 LIMIT 3")
    print("Первые 3 записи с числом очков от 500 до 2000:", res.fetchall())

    # делаем отступ 1 и выбираем первые 3 поля из таблицы, где число очков между 500 и 2000
    res = cur.execute("SELECT * FROM users WHERE score BETWEEN 500 and 2000 LIMIT 1, 3")
    print("Первые 3 записи после отступа 1 с числом очков от 500 до 2000:", res.fetchall())

    # выбираем первые 3 поля из таблицы после сортировки по очкам, где число очков между 500 и 2000
    res = cur.execute("SELECT * FROM users WHERE score BETWEEN 500 and 2000 ORDER BY score DESC LIMIT 3")
    print("Первые 3 записи после сортировки по очкам с числом очков от 500 до 2000:", res.fetchall())

    # выбираем первые 3 поля из таблицы после сортировки по очкам, где число очков более 200, с отступом 2
    res = cur.execute("SELECT * FROM users WHERE score > 200 ORDER BY score DESC LIMIT 3 OFFSET 2")
    print("Первые 3 записи после сортировки по возрастанию по очкам с числом очков от 200, отступ 2:", res.fetchall())

    # выбираем первые 5 полей из таблицы после сортировки по очкам, где число очков более 200, с отступом 1,
    # из них берем только первую запись
    res = cur.execute("SELECT * FROM users WHERE score > 200 ORDER BY score DESC LIMIT 5 OFFSET 1")
    print("Выбираем первые 5 полей из таблицы после сортировки по очкам, где число очков более 200, с отступом 1, "
          "из них берем только первую запись:", res.fetchone())

    # выбираем первые 5 полей из таблицы после сортировки по очкам, где число очков более 200, с отступом 1,
    # из них берем первые 2 записи
    res = cur.execute("SELECT * FROM users WHERE score > 200 ORDER BY score DESC LIMIT 5 OFFSET 1")
    print("выбираем первые 5 полей из таблицы после сортировки по очкам, где число очков более 200, с отступом 1, "
          "из них берем первые 2 записи:", res.fetchmany(2))

    # большое колиество записей выгоднее для памяти перебирать иттератором
    res = cur.execute("SELECT * FROM users WHERE score > 200 ORDER BY score DESC LIMIT 5 OFFSET 1")
    print("Итерировать результат INSERT экономичнее для памяти:")
    for i_elem in res:
        print(i_elem)

