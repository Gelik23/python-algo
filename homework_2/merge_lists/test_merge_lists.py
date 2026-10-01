import unittest

from .merge_lists import (
    ListNode,
    merge_with_dummy,
    merge_without_dummy,
)


def build_linked_list(values):
    head = None
    tail = None

    for value in values:
        new_node = ListNode(value)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


def linked_list_to_list(head):
    values = []

    while head is not None:
        values.append(head.value)
        head = head.next

    return values


class TestMergeLists(unittest.TestCase):
    def check_both_solutions(self, values1, values2, expected):
        list1 = build_linked_list(values1)
        list2 = build_linked_list(values2)
        result = merge_with_dummy(list1, list2)
        self.assertEqual(linked_list_to_list(result), expected)

        list1 = build_linked_list(values1)
        list2 = build_linked_list(values2)
        result = merge_without_dummy(list1, list2)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_example(self):
        self.check_both_solutions([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_both_lists_are_empty(self):
        self.check_both_solutions([], [], [])

    def test_first_list_is_empty(self):
        self.check_both_solutions([], [1, 2, 3], [1, 2, 3])

    def test_second_list_is_empty(self):
        self.check_both_solutions([1, 2, 3], [], [1, 2, 3])

    def test_lists_have_different_lengths(self):
        self.check_both_solutions([1, 5], [2, 3, 4, 6], [1, 2, 3, 4, 5, 6])

    def test_negative_values_and_duplicates(self):
        self.check_both_solutions([-5, -1, 3], [-4, -1, 2], [-5, -4, -1, -1, 2, 3])

    def test_visualization_example(self):
        values1 = [-3, 1, 4, 4, 10]
        values2 = [-2, 1, 2, 8]
        expected = [-3, -2, 1, 1, 2, 4, 4, 8, 10]

        self.check_both_solutions(values1, values2, expected)

    def test_solutions_reuse_original_nodes(self):
        for merge_function in (merge_with_dummy, merge_without_dummy):
            with self.subTest(merge_function=merge_function.__name__):
                list1 = build_linked_list([1, 3])
                list2 = build_linked_list([2, 4])
                original_node_ids = self.collect_node_ids(list1) | self.collect_node_ids(
                    list2
                )

                result = merge_function(list1, list2)

                self.assertEqual(self.collect_node_ids(result), original_node_ids)

    @staticmethod
    def collect_node_ids(head):
        node_ids = set()

        while head is not None:
            node_ids.add(id(head))
            head = head.next

        return node_ids


if __name__ == "__main__":
    unittest.main()
