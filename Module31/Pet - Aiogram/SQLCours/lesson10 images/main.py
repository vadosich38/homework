import sqlite3 as sq


def read_ava(numm: int):
    try:
        with open(f"avas/ava{numm}.jpeg", "rb") as avatar:
            return avatar.read()
    except IOError as exception:
        print("Возникла ошбка:", exception)
        return False


def write_ava(name: str, data) -> bool:
    try:
        with open(name, "wb") as out_file:
            out_file.write(data)
            return True
    except IOError as exception:
        print("Возникла ошибка:", exception)
        return False


with sq.connect("my_db.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.executescript("""
    DROP TABLE IF EXISTS users;

    CREATE TABLE IF NOT EXISTS users(
    name TEXT NOT NULL,
    ava BLOB NOT NULL,
    score INTEGER NOT NULL)""")

    # запись изображения с диска в БД
    img = read_ava(7)
    if img:
        binary = sq.Binary(img)
        cur.execute("INSERT INTO users VALUES('Николай', ?, 1000)", (binary, ))

    # запись изображеия из БД на диск
    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()['ava']

    write_ava("out_file.jpeg", img)
