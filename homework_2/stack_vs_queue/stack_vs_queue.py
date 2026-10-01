"""
Объяснение 
Сначала создаем класс Node для одного элемента связного списка. В каждом узле
храним само значение и ссылку на следующий узел.

В стеке нам достаточно хранить начало списка в переменной head. Когда вызываем
push, создаем новый узел и ставим его перед текущим head. Когда вызываем pop,
забираем значение из head и передвигаем head на следующий узел. Поэтому элемент,
который добавили последним, удаляется первым.

Для очереди храним две ссылки: head указывает на первый элемент, а tail — на
последний. enqueue добавляет новый узел после tail, а dequeue удаляет узел из
head. Поэтому элементы выходят в том же порядке, в котором мы их добавили.
Если удалили последний элемент очереди, обе ссылки снова становятся None.

Сложность
Все операции push, pop, enqueue, dequeue и peek работают за O(1), потому что
не нужно проходить по списку
Память — O(n), потому что для n значений нужно создать n узлов

Визуализация работы алгоритма
В записи состояния стека вершина находится слева, а начало очереди — слева

Стек:
операция  | состояние связного списка | результат
push(4)   | head -> 4                 | —
push(7)   | head -> 7 -> 4            | —
pop()     | head -> 4                 | вернули 7
push(9)   | head -> 9 -> 4            | —
peek()    | head -> 9 -> 4            | увидели 9, список не изменился
pop()     | head -> 4                 | вернули 9
pop()     | head -> None              | вернули 4

Очередь:
операция   | состояние связного списка        | результат
enqueue(4) | head -> 4 <- tail                | —
enqueue(7) | head -> 4 -> 7 <- tail           | —
dequeue()  | head -> 7 <- tail                | вернули 4
enqueue(9) | head -> 7 -> 9 <- tail           | —
peek()     | head -> 7 -> 9 <- tail           | увидели 7, список не изменился
dequeue()  | head -> 9 <- tail                | вернули 7
dequeue()  | head -> None, tail -> None       | вернули 9

При одинаковых добавленных значениях стек вернул 7, 9, 4, очередь — 4, 7, 9.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        node = self.head

        if node is None:
            return None

        self.head = node.next
        return node.value

    def peek(self):
        if self.head is None:
            return None

        return self.head.value

    def empty(self):
        return self.head is None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None

        node = self.head
        self.head = node.next

        if self.head is None:
            self.tail = None

        return node.value

    def peek(self):
        if self.head is None:
            return None

        return self.head.value

    def empty(self):
        return self.head is None
