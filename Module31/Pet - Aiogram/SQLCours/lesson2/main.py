import sqlite3 as sq

with sq.connect(database="my_db.db") as con:
    cur = con.cursor() #Cursor

    cur.execute("DROP TABLE IF EXISTS users") #удвлить таблицу если она существует
    #создать таблицу, если она не существует
    cur.execute("""CREATE TABLE IF NOT EXISTS users ( 
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL DEFAULT 1,
    sex INTEGER NOT NULL DEFAULT 1,
    score INTEGER NOT NULL)""")
