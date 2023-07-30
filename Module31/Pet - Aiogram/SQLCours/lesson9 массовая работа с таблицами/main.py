import sqlite3 as sq
cars = [
    ("Audi", 52642),
    ("Mercedes", 57127),
    ("Skoda", 9000),
    ("Volvo", 29000),
    ("Bentley", 350000)
]

with sq.connect("cars.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("""CREATE TABLE IF NOT EXISTS cars(
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    price INTEGER NOT NULL)""")

    # массовое добавление записей в БД
    for i_car in cars:
        cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", i_car)

    # массовое добавление записей в БД
    cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # обновление таблицы по шаблону
    cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {"Price": 0})

    # првоести несколько команд SQL в рамках одного запроса
    cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
    UPDATE cars SET price = price+1000""")
