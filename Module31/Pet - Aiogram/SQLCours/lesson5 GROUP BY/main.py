import sqlite3 as sq
import random

with sq.connect("my_db.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER DEFAULT 1,
    sex INTEGER NOT NULL DEFAULT 1,
    score INTEGER DEFAULT 0)
    """)

    cur.execute("INSERT INTO users (name, age) VALUES('Ivan', 23)")
    cur.execute("INSERT INTO users (name, age) VALUES('Anna', 23)")
    cur.execute("INSERT INTO users (name, age) VALUES('Alex', 45)")
    cur.execute("INSERT INTO users (name, age) VALUES('Allya', 4)")
    cur.execute("INSERT INTO users (name, age) VALUES('Olga', 56)")
    cur.execute("INSERT INTO users (name, age) VALUES('Alina', 32)")

    cur.execute(f"UPDATE users SET score = {random.randint(1, 100)} WHERE age > 30")
    cur.execute(f"UPDATE users SET score = {random.randint(50, 125)} WHERE age < 30")

    cur.execute("UPDATE users SET sex = 2 WHERE name LIKE '%a'")

    res = cur.execute("SELECT sum(score) as sum FROM users WHERE age > 30")
    print("Сумма баллов игроков возрастом старше 30:", res.fetchone())

    res = cur.execute("SELECT count(user_id) as count FROM users WHERE age < 30")
    print("Колиество игроков, чей возраст менее 30:", res.fetchone())

    res = cur.execute("SELECT avg(age) as avg FROM users")
    print("Среднее арифметическое врозраста игроков:", res.fetchone())

    res = cur.execute("SELECT min(age) as younger FROM users")
    print("Минимальный возраст игрока:", res.fetchone())

    res = cur.execute("SELECT max(age) as older FROM users")
    print("Максимальный возраст игрока:", res.fetchone()[0])

    res = cur.execute("SELECT count(DISTINCT name) as names FROM users")
    print("Уникальных имен в списке игроков:", res.fetchone()[0])

    res = cur.execute("SELECT DISTINCT age as unic_age FROM users")
    print("Уникальные возраста игроков:", res.fetchall())

    res = cur.execute("SELECT sum(score) as scores FROM users GROUP BY age > 30")
    print("Подсчет суммы очков по двум группам до 30 и после 30 лет", res.fetchall())

    res = cur.execute("SELECT sum(score) as scores FROM users GROUP BY sex")
    print("Сумма баллов по группам: мужчины и женщины:", res.fetchall())

    res = cur.execute("SELECT sex, sum(score) as scores FROM users GROUP BY sex ORDER BY scores DESC")
    print("Сумма баллов по группам: мужчины и женщины с сортировкой:", res.fetchall())

    res = cur.execute("SELECT sex, sum(score) as scores FROM users WHERE score > 50 GROUP BY sex")
    print("Сумма баллов по группам: мужчины и женщины в выборку взяты результаты более 50 очков:", res.fetchall())
