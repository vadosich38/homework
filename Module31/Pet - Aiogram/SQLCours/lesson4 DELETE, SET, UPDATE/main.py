import sqlite3 as sq

with sq.connect(database="my_db.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    score INTEGER DEFAULT 0)
    """)

    cur.execute("INSERT INTO users (name, age, sex) VALUES('Ivan', 23, 1)")
    cur.execute("INSERT INTO users (name, age, sex) VALUES('Alex', 3, 1)")
    cur.execute("INSERT INTO users (name, age, sex) VALUES('Olha', 33, 2)")
    cur.execute("INSERT INTO users (name, age, sex) VALUES('Katya', 25, 2)")
    cur.execute("INSERT INTO users (name, age, sex) VALUES('Stepan', 26, 1)")
    cur.execute("INSERT INTO users (name, age, sex) VALUES('Snejana', 21, 2)")
    cur.execute("INSERT INTO users (name, age, sex) VALUES('Max', 12, 1)")
    cur.execute("INSERT INTO users (name, age, sex) VALUES('Lida', 43, 2)")
    cur.execute("INSERT INTO users (name, age, sex) VALUES('Tanya', 53, 2)")

    cur.execute("UPDATE users SET sex = 1") # всем установил пол "1"
    cur.execute("UPDATE users SET score = 123 WHERE name = 'Ivan'") # Ивану присвоил 123 очка
    cur.execute("UPDATE users SET score = score + 200 WHERE age < 20" )# Всем младще 20ти добавил 200 очков
    cur.execute("UPDATE users SET score = score - 10 WHERE name LIKE 'Ivan'") # все у кого имя в точности ИВАН отнять 10
    cur.execute("UPDATE users SET score = 0 WHERE name LIKE 'I__n'") # Все у кого имя начинается на И потом 2 любых символа и окончание н, очки установить на 0
    cur.execute("UPDATE users SET score = 190 WHERE name LIKE 'S%'") #все у кого имя начинается на S и с любым проболжением установить очки на 190
    cur.execute("UPDATE users SET score = 8, age = 8 WHERE name LIKE 'Olha' and age = 33") #у кого имя ольга и возраст 33, изменить очки и возраст на 8

    cur.execute("DELETE from users WHERE name LIKE 'Lida'") # удалить строку, где имя равно Лида

