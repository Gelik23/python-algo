"""
Объяснение
У нас есть два списка, и числа в каждом уже идут по порядку. Сравниваем первые
узлы list1 и list2 и берем тот, у которого значение меньше. Добавляем этот узел
в конец результата и переходим к следующему узлу в том же списке. Повторяем,
пока один из списков не закончится. Оставшуюся часть второго списка можно сразу
присоединить к результату, потому что она уже отсортирована.

В первом способе сначала создаем временный узел dummy. Он нужен только для того,
чтобы первый настоящий узел добавлялся так же, как все остальные. Сам dummy в
ответ не попадает, потому что в конце возвращаем dummy.next.

Во втором способе dummy нет, поэтому первый узел результата выбираем отдельно.
После этого остальные узлы добавляем точно так же. В обоих способах новые узлы
для значений не создаем, а соединяем узлы из исходных списков.

Сложность
O(n + m) по времени: проходим по каждому узлу list1 и list2 только один раз
O(1) дополнительной памяти: новые списки не создаем, а только меняем ссылки next
между существующими узлами. Временный dummy занимает постоянное место

Визуализация работы алгоритма
Возьмем списки разной длины, где есть отрицательные числа и повторы
list1: -3 -> 1 -> 4 -> 4 -> 10
list2: -2 -> 1 -> 2 -> 8

сравниваем | берем узел      | объединенный список
-3 и -2   | -3 из list1      | -3
1 и -2    | -2 из list2      | -3 -> -2
1 и 1     | 1 из list1       | -3 -> -2 -> 1
4 и 1     | 1 из list2       | -3 -> -2 -> 1 -> 1
4 и 2     | 2 из list2       | -3 -> -2 -> 1 -> 1 -> 2
4 и 8     | первый 4 list1   | -3 -> -2 -> 1 -> 1 -> 2 -> 4
4 и 8     | второй 4 list1   | -3 -> -2 -> 1 -> 1 -> 2 -> 4 -> 4
10 и 8    | 8 из list2       | -3 -> -2 -> 1 -> 1 -> 2 -> 4 -> 4 -> 8

list2 закончился, поэтому одним присваиванием tail.next = list1 присоединяем
оставшийся узел 10. Итог: -3 -> -2 -> 1 -> 1 -> 2 -> 4 -> 4 -> 8 -> 10.
Оба способа дают этот результат; различается только выбор первого узла.
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_with_dummy(list1, list2):
    dummy = ListNode(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


def merge_without_dummy(list1, list2):
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.value <= list2.value:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    tail = head

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return head
