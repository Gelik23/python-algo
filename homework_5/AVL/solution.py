"""
Задача 3. AVL

Как решаем
-------------
Обычное дерево поиска может вытянуться в цепочку. Тогда поиск станет
похож на просмотр списка. В AVL у каждого узла
высоты левого и правого поддеревьев отличаются не больше чем на 1.

В Node храним значение, ссылки на детей и высоту. Высота пустого дерева 0,
у листа высота 1. Высота узла равна 1 + max(высоты детей).
Разницу высот считаем как высота слева минус высота справа.
Если она равна -1, 0 или 1, ничего менять не нужно.

Ищем как в BST. Если значение меньше текущего, идем влево, если больше,
идем вправо.
Возвращаем True, если нашли значение, иначе False.
Вставка сначала находит свободное место как в BST. Повтор игнорируем.
На обратном пути рекурсии обновляем высоты и восстанавливаем баланс.
insert и delete изменяют дерево и ничего не возвращают.

Повороты
---------
Если слева стало слишком высоко, делаем правый поворот.
Если справа, делаем левый. Иногда высокая ветка сначала идет в одну
сторону, а потом в другую. Тогда сначала поворачиваем ребенка,
а потом сам узел. Получаем четыре случая.
LL исправляем правым поворотом, RR левым.
Для LR сначала делаем левый поворот у ребенка, потом правый у узла.
Для RL сначала правый у ребенка, потом левый у узла.

Поворот возвращает новый корень поддерева. Среднее поддерево переносим
между узлами, а не теряем. Например, при правом повороте левый ребенок
поднимается, старый корень опускается вправо, а правое поддерево поднятого
узла становится левым поддеревом старого корня.
Сначала обновляем высоту опущенного узла, затем поднятого.

Удаление
---------
Сначала находим значение. Если его нет, дерево не меняется.
Если это лист, возвращаем None. Если ребенок один, возвращаем его.
Если детей два, ищем самое маленькое значение справа. Оно идет следующим
после удаляемого при обходе по возрастанию. Копируем это значение в узел
и удаляем прежний экземпляр из правого поддерева.
Затем восстанавливаем баланс у каждого предка на обратном пути.
В отличие от вставки, при удалении исправления могут понадобиться
в нескольких местах на пути к корню.

Почему это работает
-----------------------
Вставка и удаление сохраняют порядок BST. Повороты меняют связи,
но сохраняют порядок значений при inorder-обходе. Затем у каждого
предка на пути к корню пересчитываем высоту и исправляем перевес.
Поэтому после операции сохраняются и порядок BST, и баланс AVL.
Работаем с целыми числами, включая отрицательные. Одинаковые не храним.

Визуализация. поворот внутри дерева, удаление корня и новый поворот
------------------------------------------------------------------
Вставляем [50, 30, 70, 10, 40, 60, 80, 20].

50
├── L: 30
│   ├── L: 10
│   │   └── R: 20
│   └── R: 40
└── R: 70
    ├── L: 60
    └── R: 80

Шаг 1. Добавляем 15. Идем 50 -> 30 -> 10 -> 20 -> влево.
На обратном пути сначала проверяем нижние узлы.
Узел | Высота слева | Высота справа | Баланс
15   | 0            | 0             | 0
20   | 1            | 0             | 1
10   | 0            | 2             | -2

У 10 перевес вправо, у его правого ребенка 20 влево. Это RL.
Ни 50, ни 30 пока не поворачиваем. Исправляем именно поддерево 10.

До исправления        Поворот вправо у 20   Поворот влево у 10
10                    10                   15
└── R: 20             └── R: 15             ├── L: 10
    └── L: 15             └── R: 20         └── R: 20

Новый корень 15 сохраняем в левом ребенке 30. Получаем такое дерево.

50
├── L: 30
│   ├── L: 15
│   │   ├── L: 10
│   │   └── R: 20
│   └── R: 40
└── R: 70
    ├── L: 60
    └── R: 80

У 30 высоты 2 и 1, у 50 высоты 3 и 2. Других поворотов не нужно.

Шаг 2. Удаляем корень 50. Детей два, поэтому ищем минимум справа.
Идем 70 -> 60. Минимум находится глубже, а не в самом правом ребенке.
Переносим 60 в корень и удаляем старый узел 60 из-под 70.

60
├── L: 30
│   ├── L: 15
│   │   ├── L: 10
│   │   └── R: 20
│   └── R: 40
└── R: 70
    └── R: 80

У 70 высоты 0 и 1, у 60 высоты 3 и 2. Баланс еще допустимый.

Шаг 3. Удаляем 80. Правая сторона корня стала ниже.
Узел | Высота слева | Высота справа | Баланс
70   | 0            | 0             | 0
60   | 3            | 1             | 2
30   | 2            | 1             | 1

У 60 перевес слева, левый ребенок 30 тоже наклонен влево.
Поворачиваем 60 вправо. Поддерево 40 раньше было справа от 30,
теперь переносим его влево от 60. Иначе потеряем узлы или нарушим
порядок значений в дереве.

30
├── L: 15
│   ├── L: 10
│   └── R: 20
└── R: 60
    ├── L: 40
    └── R: 70

Теперь высоты детей корня 2 и 2, высота всего дерева 3.
В этом примере сделали два вида поворотов на разных уровнях,
заменили корень следующим значением и перенесли непустое поддерево.
Ищем 40. Сначала 40 > 30, идем вправо к 60. Потом 40 < 60, идем влево
и находим 40.
Ищем удаленное 50. Идем вправо к 60, влево к 40, вправо в None.
Получаем False.

Сложность
----------
Высота AVL равна O(log n), где n обозначает количество узлов.
Поиск занимает O(log n) времени и O(1) дополнительной памяти, используем цикл.
Вставка занимает O(log n) времени и O(log n) памяти для рекурсивных вызовов.
Удаление занимает O(log n) времени и O(log n) памяти для рекурсивных вызовов.
Ищем successor тоже по пути дерева, поэтому оценка удаления не меняется.
Каждый поворот занимает O(1), так как меняет постоянное число ссылок.
Само дерево занимает O(n) памяти.
Inorder занимает O(n) времени. Для стека нужно O(log n) памяти,
для списка результата O(n).
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node is not None else 0

    def _update_height(self, node):
        node.height = 1 + max(
            self._height(node.left),
            self._height(node.right),
        )

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node):
        new_root = node.left
        middle = new_root.right
        new_root.right = node
        node.left = middle
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        middle = new_root.left
        new_root.left = node
        node.right = middle
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node
        return self._rebalance(node)

    def search(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return self._rebalance(node)

    def inorder(self):
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append(node.value)
            visit(node.right)

        visit(self.root)
        return result
