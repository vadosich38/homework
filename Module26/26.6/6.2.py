from typing import Any
from typing import Optional


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.node = None
        self.i = 1

    def __str__(self) -> str:
        answer = ""
        if self.head:
            node = self.head
            while node.next_node:
                answer += str(node.element) + "\n"
                node = node.next_node
            else:
                answer += str(node.element) + "\n"
                return answer
        else:
            return answer

    def __iter__(self) -> 'LinkedList':
        self.i = 1
        self.node = self.head
        return self

    def __next__(self) -> Any:
        lenth = self.lenth()

        if self.i <= lenth:
            if self.i == 1:
                self.i += 1
                return self.node.element
            else:
                self.i += 1
                self.node = self.node.next_node
                return self.node.element
        else:
            raise StopIteration

    def lenth(self) -> int:
        i = 0
        node = self.head

        while node.next_node:
            i += 1
            node = node.next_node
        else:
            i += 1
            return i

    def append(self, element: Any) -> None:
        if not self.head:
            self.head = Node(element=element)
            return

        else:
            node = self.head

            while node.next_node:
                node = node.next_node
            else:
                node.next_node = Node(element=elem)

    def get(self, index: int) -> Any:
        i = 1
        node = self.head

        while True:
            if i == index:
                return print(str(node.element) + "\n")
            else:
                if node.next_node:
                    node = node.next_node
                    i += 1
                elif index > i:
                    raise IndexError

    def remove(self, index: int) -> None:
        i = 1
        node = self.head
        prev_node = node

        while True:
            if i == index == 1:
                self.head = node.next_node
                del node
                return
            elif i == index and not node.next_node:
                prev_node.next_node = None
                del node
                return
            elif i == index:
                prev_node.next_node = node.next_node
                del node
                return

            else:
                if node.next_node:
                    prev_node = node
                    node = node.next_node
                    i += 1
                elif index > i:
                    raise IndexError


class Node:
    def __init__(self, element: Any, next_node: Optional['Node', None] = None) -> None:
        self.element = element
        self.next_node = next_node


my_list = LinkedList()
my_list.append(1)
my_list.append(10)
my_list.append(100)
my_list.append(1000)
print(my_list)
my_list.get(index=1)
my_list.remove(1)
print(my_list)

print("Цикл:")
for elem in my_list:
    print(elem)
