import sqlite3 as sq
cars = [
    ("Audi", 52642),
    ("Mercedes", 57127),
    ("Skoda", 9000),
    ("Volvo", 29000),
    ("Bentley", 350000)
]
con = None

try:
    con = sq.connect("cars.db")
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("DROP TABLE IF EXISTS cust")

    cur.executescript("""
        CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        price INTEGER NOT NULL);
        
        CREATE TABLE IF NOT EXISTS cust(
        name TEXT NOT NULL,
        trade_in INTEGER,
        buy INTEGER);
        
        BEGIN;
        
        INSERT INTO cars VALUES (NULL, 'Audi', 52642);
        INSERT INTO cars VALUES (NULL, 'Mercedes', 57127);
        INSERT INTO cars VALUES (NULL, 'Skoda', 9000);
        INSERT INTO cars VALUES (NULL, 'Volvo', 29000);
        INSERT INTO cars VALUES(NULL, 'Bentley', 350000);
        UPDATE cars SET price = price+1000""")

    cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    last_id = cur.lastrowid
    buy_car_id = 2
    cur.execute("INSERT INTO cust VALUES('Федор', ?, ?)", (last_id, buy_car_id))

    con.commit() # сохранить изменения в БД

except sq.Error as e:
    if con:
        con.rollback() #откатить изменения в БД если возникла ошибка
        print("Возникла ошибка выполнения запроса")
finally:
    if con:
        con.close() # закрыть БД
