class Steck:

    def __init__(self):
        self.__correct = 0
        self.__my_stack = list()

    def __str__(self):
        return "; ".join(self.__my_stack)

    def add(self, elem):
        self.__my_stack.append(elem)

    def search(self, elem):
        if len(self.__my_stack) > 0:
            index = self.__my_stack.index(elem)
            return index
        else:
            print("Этот стек пустой!")

    def delete(self):
        del self.__my_stack[-1]

    def get_elem(self):
        return self.__my_stack[-1]


class TaskManager:
    def __init__(self):
        self.__my_task_list = dict()
        self.__flag = False

    def __str__(self):
        display = []
        if self.__my_task_list:
            for i_priority in sorted(self.__my_task_list.keys()):
                display.append("{prior} {task}\n".format(prior=str(i_priority), task=self.__my_task_list[i_priority]))
        return "".join(display)

    def add_task(self, task, priority):
        if priority not in self.__my_task_list:
            self.__my_task_list[priority] = Steck()
        self.__my_task_list[priority].add(task)
        print("Задача '{}' успешно добавлена в список задач с приоритетом {}\n".format(task, priority))
        print(self.__my_task_list[priority])

    def delete_task(self, priority):
        try:
            task = self.__my_task_list[priority].get_elem()
            self.__my_task_list[priority].delete()
            print("Задача {} успешно удалена!\n".format(task))
        except Exception as a:
            print("Удаление не завершено из-за ошибки:", a)

    def complete_task(self, priority):
        try:
            task = self.__my_task_list[priority].get_elem()
            self.__my_task_list[priority].delete()
            print("Задача {} успешно выполнена!\n".format(task))
        except Exception as a:
            print("Выполнить задачу не удалось из-за ошибки:", a, "\n")


my_list = TaskManager()
while True:
    action = input("Что хотите сделать?\n'+' чтобы добавить задачу, '-' чтобы удалить задачу, 'x' чтобы выполнить "
                   "задачу, 'o' чтобы посмотреть список задач: ")
    if action == "+":
        task = input("Напишите задачу: ")
        priority = int(input("Введите приоритет этой задачи (от 1 до 5): "))
        my_list.add_task(task=task.capitalize(), priority=priority)
    elif action == "-":
        priority = int(input("Задачу с каким приоритетом удалить: "))
        my_list.delete_task(priority=priority)
    elif action == "x":
        priority = int(input("Задачу с каким приоритетом выполнить: "))
        my_list.complete_task(priority=priority)
    elif action == "o":
        print(my_list)
    else:
        print("Неверный ввод! Попробуйте еще раз...\n")