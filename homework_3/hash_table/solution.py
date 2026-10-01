"""
Задача: собственная хеш-таблица методом цепочек

Идея алгоритма
---------------
Хеш-таблица состоит из массива buckets. Каждая ячейка массива
хранит начало односвязного списка.

Узел списка Node хранит:
    key   — ключ,
    value — значение,
    hash  — заранее вычисленный хеш ключа,
    next  — ссылку на следующий узел.

Для ключа вычисляем:
    hash_value = hash(key)
    bucket_index = hash_value % capacity

Если несколько ключей попадают в один bucket,
они хранятся в одном связном списке.
Это позволяет разрешать коллизии методом цепочек.


Добавление / обновление
-----------------------
1. Вычисляем индекс bucket.
2. Проходим по цепочке:
   - если ключ уже существует, обновляем value;
   - иначе создаем новый Node и добавляем его в начало списка.
3. Проверяем коэффициент заполнения.
4. Если load factor превышает 0.75, выполняем rehash.


Поиск
-----
1. Вычисляем bucket.
2. Проходим только по соответствующему связному списку.
3. Сравниваем ключи узлов с искомым ключом.
4. Если ключ найден — возвращаем value.
5. Иначе считаем, что элемента нет.


Удаление
--------
Для удаления элемента из середины цепочки меняем ссылки:

A -> B -> C

Удаляем B:

A.next = B.next

Получаем:

A -> C


Если удаляется первый элемент цепочки,
bucket начинает указывать на следующий узел.


Rehash
------
При увеличении load factor цепочки становятся длиннее,
поэтому создается новый массив buckets большего размера.

Все существующие элементы перераспределяются:

new_index = node.hash % new_capacity

Хеш ключа можно использовать повторно,
но индекс bucket необходимо вычислить заново,
так как изменилось количество bucket.


Оценка сложности
----------------
Средний случай:
    put    — O(1)
    get    — O(1)
    remove — O(1)

Худший случай:
    все элементы попали в одну цепочку:

    put/get/remove — O(n)

Rehash занимает O(n), так как все элементы
нужно перераспределить.

Память:
    O(n + capacity)


Визуализация
-------------
capacity = 4

bucket 1:

("cat", 10, hash=5)
        |
        v
("car", 20, hash=9)
        |
        v
("cup", 30, hash=13)


Поиск "car":

1. hash("car") % 4 -> bucket 1
2. Проверяем "cat" — не подходит
3. Переходим по next
4. Находим "car" и возвращаем 20


Удаление "car":

cat -> car -> cup

prev = cat
current = car

prev.next = current.next

Получаем:

cat -> cup
"""




class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)
        self.next = None


class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity
        self.max_load_factor = 0.75

    def _get_index(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._get_index(key)

        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        node = Node(key, value)
        node.next = self.buckets[index]
        self.buckets[index] = node
        self.size += 1

        if self.size / self.capacity > self.max_load_factor:
            self._rehash()

    def get(self, key):
        index = self._get_index(key)

        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def remove(self, key):
        index = self._get_index(key)

        current = self.buckets[index]
        previous = None

        while current is not None:
            if current.key == key:
                if previous is None:
                    self.buckets[index] = current.next
                else:
                    previous.next = current.next

                self.size -= 1
                return current.value

            previous = current
            current = current.next

        raise KeyError(key)

    def _rehash(self):
        old_buckets = self.buckets

        self.capacity *= 2
        self.buckets = [None] * self.capacity

        for bucket in old_buckets:
            current = bucket

            while current is not None:
                self._insert_without_resize(current)
                current = current.next

    def _insert_without_resize(self, node):
        index = node.hash % self.capacity

        new_node = Node(node.key, node.value)
        new_node.hash = node.hash
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node

    def __len__(self):
        return self.size
