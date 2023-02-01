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


stack1 = Steck()

stack1.add("ad")
stack1.add("w")
stack1.add("qd")
stack1.add("td")


print("\nЭлемент '{elem}' находится в стеке под номером {key}".format(elem="td", key=stack1.search(elem="td")))
stack1.delete(elem="ad111")
stack1.delete(elem="ad")

print("Элемент '{elem}' на ходится в стеке под номером {key}".format(elem="td", key=stack1.search(elem="td")))

print("Распечатываю стек:", stack1)

stack1.add("oop")
print("Элемент '{elem}' на ходится в стеке под номером {key}".format(elem="td", key=stack1.search(elem="td")))
print("Элемент '{elem}' на ходится в стеке под номером {key}".format(elem="oop", key=stack1.search(elem="oop")))

