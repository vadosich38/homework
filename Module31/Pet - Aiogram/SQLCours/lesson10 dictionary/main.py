import sqlite3 as sq
cars = [
    ("Audi", 52642),
    ("Mercedes", 57127),
    ("Skoda", 9000),
    ("Volvo", 29000),
    ("Bentley", 350000)
]

with sq.connect("my_db.db") as con:
    con.row_factory = sq.Row #чтобы преобразовать в словарь выдачу от запроса к БД
    cur = con.cursor()

    cur.executescript("""
    DROP TABLE IF EXISTS cars;
    
    CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    price INTEGER NOT NULL)""")

    cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    res = cur.execute("SELECT * FROM cars") # перебор циклом выбранных значений из табилцы базы данных
    for i_elem in res:
        print(f"id: {i_elem['id']}, model: {i_elem['model']}, price: {i_elem['price']}")
