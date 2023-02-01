class Steck:
    __my_stack = dict()

    def __init__(self):
        self.__correct = 0

    def __str__(self):
        return self.__my_stack[len(self.__my_stack)]

    def set_correct(self, count):
        self.__correct += count

    def get_correct(self):
        return self.__correct

    def add(self, elem):
        key = len(self.__my_stack)
        self.__my_stack[key+1] = elem
        print("Элемент '{}' успешно добавлен в стек под номером {}!".format(elem, key+1))

    def search(self, elem):
        max_index = len(self.__my_stack)
        for key in range(max_index, 0, -1):
            if self.__my_stack[key] == elem:
                return key
        else:
            return f"Элемент '{elem}' не найден!"

    def delete(self, elem):
        search_res = self.search(elem)
        if search_res == f"Элемент '{elem}' не найден!":
            print("Ошибка удаления:", search_res)
        else:
            stack_len = len(self.__my_stack)
            del self.__my_stack[search_res]
            for i_key in range(1, stack_len+1):
                try:
                    temp = self.__my_stack[i_key]
                    del self.__my_stack[i_key]
                    self.__my_stack[i_key - self.get_correct()] = temp
                except KeyError:
                    self.set_correct(count=1)
            else:
                self.set_correct(-self.get_correct())
                print("Элемент '{}' успешно удален из стека!".format(elem))


class TaskManager:
    def __init__(self):
        self.__my_task_list = dict()
        self.__5priority = list()
        self.__4priority = list()
        self.__3priority = list()
        self.__2priority = list()
        self.__1priority = list()
        self.__flag = False

    def __str__(self):
        self.__sort_tasks()
        flag = True
        return "\nЗадачи с приоритетом 1: {}" \
               "\nЗадачи с приоритетом 2: {}" \
               "\nЗадачи с приоритетом 3: {}" \
               "\nЗадачи с приоритетом 4: {}" \
               "\nЗадачи с приоритетом 5: {}\n".format(self.__1priority, self.__2priority, self.__3priority,
                                                     self.__4priority, self.__5priority)

    def reload(self):
        self.__1priority = list()
        self.__2priority = list()
        self.__3priority = list()
        self.__4priority = list()
        self.__5priority = list()

    def get_flag(self):
        return self.__flag

    def __sort_tasks(self):
        for i_key, i_value in self.__my_task_list.items():
            if i_value == 5:
                self.__5priority.append(i_key)
            elif i_value == 4:
                self.__4priority.append(i_key)
            elif i_value == 3:
                self.__3priority.append(i_key)
            elif i_value == 2:
                self.__2priority.append(i_key)
            elif i_value == 1:
                self.__1priority.append(i_key)

    def add_task(self, task, priority):
        self.__my_task_list[task] = priority
        print("Задача '{}' успешно добавлена в список задач с приоритетом {}\n".format(task, priority))

    def delete_task(self, task):
        try:
            del self.__my_task_list[task]
            print("Задача {} успешно удалена!\n".format(task))
        except KeyError:
            print("Такая задача не найдена и удалить ее невозможно!")

    def complete_task(self, task):
        try:
            del self.__my_task_list[task]
            print("Задача {} успешно выполнена, вы молодец!\n".format(task))
        except KeyError:
            print("Такая задача не найдена и выполнить ее невозможно!")


my_list = TaskManager()
while True:
    if my_list.get_flag():
        my_list.reload()

    action = input("Что хотите сделать?\n'+' чтобы добавить задачу, '-' чтобы удалить задачу, 'x' чтобы выполнить "
                   "задачу, 'o' чтобы посмотреть список задач: ")
    if action == "+":
        task = input("Напишите задачу: ")
        priority = int(input("Введите приоритет этой задачи (от 1 до 5): "))
        my_list.add_task(task=task.capitalize(), priority=priority)
    elif action == "-":
        task = input("Какую задачу нужно удалить: ")
        my_list.delete_task(task=task.capitalize())
    elif action == "x":
        task = input("Какую задачу вы выполнили: ")
        my_list.complete_task(task=task.capitalize())
    elif action == "o":
        print(my_list)
    else:
        print("Неверный ввод! Попробуйте еще раз...\n")