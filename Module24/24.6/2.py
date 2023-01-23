import statistics


class Student:

    def __init__(self, st_name, gr_num, marks):
        self.name = st_name
        self.group_n = gr_num
        self.marks_list = marks


def my_input():
    name = input("Введите имя студента: ")
    gr_numm = input("Введите номер группы студента: ")
    try:
        marks_list = list(map(int, input("Введите оценки студента через запятую: ").split(", ")))
    except Exception as x:
        print("Ошибка по причине:", x, "Попробуйте еще раз!")
        marks_list = list(map(int, input("Введите оценки студента через запятую: ").split(", ")))
    finally:
        print()
    return name, gr_numm, marks_list


def avg(my_list):
    summ = 0
    for i_elem in my_list:
        summ += int(i_elem)
    avg_num = summ / len(my_list)
    return avg_num


students = list(Student(*my_input()) for _ in range(2))
students.sort(key=lambda x: statistics.mean(x.marks_list), reverse=True)

print("Рейтинг студентов от преуспеващих до отстающих:")
for i_student in students:
    print("{}. Средний бал студента: {}".format(i_student.name, avg(i_student.marks_list)))
