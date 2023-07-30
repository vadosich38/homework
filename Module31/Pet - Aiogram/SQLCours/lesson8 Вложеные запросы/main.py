import sqlite3 as sq

with sq.connect("my_db.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS marks")
    cur.execute("DROP TABLE IF EXISTS students")
    cur.execute("DROP TABLE IF EXISTS female")

    cur.execute("""CREATE TABLE IF NOT EXISTS marks(
                id INTEGER NOT NULL,
                subject TEXT NOT NULL,
                mark INTEGER NOT NULL)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex INTEGER NOT NULL,
                old INTEGER NOT NULL)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS female(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex INTEGER NOT NULL,
                old INTEGER NOT NULL)""")

    cur.execute("INSERT INTO students VALUES(NULL, 'Коля', 1, 17)")
    cur.execute("INSERT INTO students VALUES(NULL, 'Маша', 2, 18)")
    cur.execute("INSERT INTO students VALUES(NULL, 'Вася', 1, 19)")
    cur.execute("INSERT INTO students VALUES(NULL, 'Даша', 2, 17)")

    cur.execute("INSERT INTO marks VALUES(1, 'Си', 4)")
    cur.execute("INSERT INTO marks VALUES(1, 'Физика', 3)")
    cur.execute("INSERT INTO marks VALUES(1, 'Вышка', 5)")
    cur.execute("INSERT INTO marks VALUES(1, 'Физра', 5)")
    cur.execute("INSERT INTO marks VALUES(2, 'Си', 3)")
    cur.execute("INSERT INTO marks VALUES(2, 'Вышка', 4)")
    cur.execute("INSERT INTO marks VALUES(2, 'Химия', 3)")
    cur.execute("INSERT INTO marks VALUES(3, 'Си', 4)")
    cur.execute("INSERT INTO marks VALUES(3, 'Черчение', 3)")
    cur.execute("INSERT INTO marks VALUES(3, 'Физика', 5)")

    # узнаем оценку конкретного студента по конкретному предмету
    res1 = cur.execute("SELECT mark FROM marks WHERE id = 2 and subject = 'Си'")

    # узнаем айди студентов у кого оценка по конкретному предмету выше чем по тому же предмету у выбраного студента
    res2 = cur.execute("""SELECT id FROM marks WHERE subject = 'Си'
                      and mark > (SELECT mark FROM marks WHERE id = 2 and subject = 'Си')""")

    # узнаем имя, предмет и оценку студентов, у кого оценка по любому предету выше чем у выбранного студента
    # по выбраному предмету (вложеный запрос!)
    res3 = cur.execute("""SELECT name, subject, mark FROM marks 
                        JOIN students ON students.rowid == marks.id
                        WHERE subject LIKE 'Си' and mark > (SELECT mark FROM marks WHERE id = 2 and subject LIKE 'Си')""")
    # print(res3.fetchall())

    # наполняем таблицу female из таблицы students по фильтру пол равен 2
    cur.execute("""INSERT INTO female SELECT NULL, name, sex, old FROM students WHERE sex = 2""")

    # обнуляем все оценки в таблице marks, которые меньше или равны минимальной оценке студента с id = 1
    cur.execute("""UPDATE marks SET mark = 0 WHERE mark <= (SELECT min(mark) FROM marks WHERE id = 1)""")

    # из таблицы students удалить всех студентов младше Маши
    cur.execute("""DELETE FROM students WHERE old < (SELECT old FROM students WHERE name LIKE 'Маша')""")
