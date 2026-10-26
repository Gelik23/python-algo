import unittest

from solution import (
    BST, Node, inorder, is_balanced, is_valid_bst, postorder, preorder,
    reverse_inorder, reverse_postorder, reverse_preorder,
)


TRAVERSALS = [
    preorder, inorder, postorder,
    reverse_preorder, reverse_inorder, reverse_postorder,
]


def build_bst(values):
    tree = BST()
    for value in values:
        tree.insert(value)
    return tree


class TestBST(unittest.TestCase):
    def test_empty_tree(self):
        tree = BST()
        self.assertIsNone(tree.root)
        for traversal in TRAVERSALS:
            with self.subTest(traversal=traversal.__name__):
                self.assertEqual(traversal(tree.root), [])

    def test_single_node(self):
        tree = build_bst([5])
        for traversal in TRAVERSALS:
            with self.subTest(traversal=traversal.__name__):
                self.assertEqual(traversal(tree.root), [5])

    def test_visualization_example_all_traversals(self):
        tree = build_bst([8, 3, 10, 1, 6, 14, 4, 7, 13])
        expected = [
            [8, 3, 1, 6, 4, 7, 10, 14, 13],
            [1, 3, 4, 6, 7, 8, 10, 13, 14],
            [1, 4, 7, 6, 3, 13, 14, 10, 8],
            [8, 10, 14, 13, 3, 6, 7, 4, 1],
            [14, 13, 10, 8, 7, 6, 4, 3, 1],
            [13, 14, 10, 7, 4, 6, 1, 3, 8],
        ]
        for traversal, result in zip(TRAVERSALS, expected):
            with self.subTest(traversal=traversal.__name__):
                self.assertEqual(traversal(tree.root), result)
        self.assertEqual(tree.root.left.right.left.value, 4)
        self.assertEqual(tree.root.right.right.left.value, 13)
        self.assertTrue(is_valid_bst(tree.root))

    def test_duplicates_are_ignored(self):
        tree = build_bst([5, 3, 7, 5, 3, 7])
        self.assertEqual(inorder(tree.root), [3, 5, 7])

    def test_negative_values_and_zero(self):
        tree = build_bst([0, -3, 5, -1, -10])
        self.assertEqual(inorder(tree.root), [-10, -3, -1, 0, 5])
        self.assertTrue(is_valid_bst(tree.root))

    def test_sorted_and_reverse_sorted_insertions(self):
        for values in [list(range(200)), list(range(199, -1, -1))]:
            with self.subTest(first=values[0]):
                tree = build_bst(values)
                self.assertEqual(inorder(tree.root), list(range(200)))
                self.assertEqual(preorder(tree.root), values)
                self.assertEqual(postorder(tree.root), values[::-1])
                self.assertTrue(is_valid_bst(tree.root))

    def test_traversals_on_non_bst(self):
        root = Node(1)
        root.left = Node(9)
        root.right = Node(0)
        self.assertEqual(inorder(root), [9, 1, 0])
        self.assertEqual(preorder(root), [1, 9, 0])
        self.assertEqual(postorder(root), [9, 0, 1])
        self.assertEqual(reverse_inorder(root), [0, 1, 9])
        self.assertEqual(reverse_preorder(root), [1, 0, 9])
        self.assertEqual(reverse_postorder(root), [0, 9, 1])

    def test_result_lists_are_independent(self):
        tree = build_bst([2, 1, 3])
        for traversal in TRAVERSALS:
            with self.subTest(traversal=traversal.__name__):
                first = traversal(tree.root)
                expected = first.copy()
                first.append(99)
                self.assertEqual(traversal(tree.root), expected)


class TestValidateBST(unittest.TestCase):
    def test_empty_and_single(self):
        self.assertTrue(is_valid_bst(None))
        self.assertTrue(is_valid_bst(Node(0)))

    def test_correct_tree(self):
        self.assertTrue(is_valid_bst(build_bst([10, 5, 15, 2, 7, 12, 20]).root))

    def test_incorrect_direct_child(self):
        for side, value in [('left', 11), ('right', 9)]:
            with self.subTest(side=side):
                root = Node(10)
                setattr(root, side, Node(value))
                self.assertFalse(is_valid_bst(root))

    def test_hidden_violation_on_left(self):
        root = Node(10)
        root.left = Node(5)
        root.left.left = Node(2)
        root.left.right = Node(12)
        root.right = Node(15)
        self.assertFalse(is_valid_bst(root))

    def test_hidden_violation_on_right(self):
        root = Node(10)
        root.right = Node(15)
        root.right.left = Node(7)
        self.assertFalse(is_valid_bst(root))

    def test_equal_values_are_invalid(self):
        for side in ['left', 'right']:
            with self.subTest(side=side):
                root = Node(5)
                setattr(root, side, Node(5))
                self.assertFalse(is_valid_bst(root))
        root = Node(10)
        root.left = Node(5)
        root.left.right = Node(10)
        self.assertFalse(is_valid_bst(root))

    def test_large_integers(self):
        root = Node(0)
        root.left = Node(-(10 ** 100))
        root.right = Node(10 ** 100)
        self.assertTrue(is_valid_bst(root))


class TestBalancedTree(unittest.TestCase):
    def test_empty_and_single(self):
        self.assertTrue(is_balanced(None))
        self.assertTrue(is_balanced(Node(1)))

    def test_two_nodes(self):
        for values in [[1, 2], [2, 1]]:
            with self.subTest(values=values):
                self.assertTrue(is_balanced(build_bst(values).root))

    def test_visualization_balanced(self):
        self.assertTrue(is_balanced(build_bst([4, 2, 6, 1, 3]).root))

    def test_perfect_tree(self):
        self.assertTrue(is_balanced(build_bst([4, 2, 6, 1, 3, 5, 7]).root))

    def test_three_node_chains(self):
        for values in [[1, 2, 3], [3, 2, 1]]:
            with self.subTest(values=values):
                self.assertFalse(is_balanced(build_bst(values).root))

    def test_hidden_imbalance(self):
        root = build_bst([10, 5, 3, 1, 15, 20, 25]).root
        self.assertFalse(is_balanced(root))

    def test_right_subtree_imbalance(self):
        root = build_bst([10, 5, 3, 7, 15, 20, 25]).root
        self.assertFalse(is_balanced(root))

    def test_balance_does_not_require_bst(self):
        root = Node(0)
        root.left = Node(10)
        root.right = Node(-10)
        self.assertTrue(is_balanced(root))
        self.assertFalse(is_valid_bst(root))

    def test_larger_balanced_tree(self):
        def build_perfect(start, end):
            if start >= end:
                return None
            middle = (start + end) // 2
            node = Node(middle)
            node.left = build_perfect(start, middle)
            node.right = build_perfect(middle + 1, end)
            return node

        root = build_perfect(0, 1023)
        self.assertTrue(is_balanced(root))
        self.assertTrue(is_valid_bst(root))
        self.assertEqual(inorder(root), list(range(1023)))


class TestUnusualVisualizationExamples(unittest.TestCase):
    def test_asymmetric_tree_with_duplicates(self):
        values = [0, -12, 15, -20, -4, 9, 23, -8, -1, 11, 18, -6, 10, -8, 0]
        root = build_bst(values).root
        expected = [
            [0, -12, -20, -4, -8, -6, -1, 15, 9, 11, 10, 23, 18],
            [-20, -12, -8, -6, -4, -1, 0, 9, 10, 11, 15, 18, 23],
            [-20, -6, -8, -1, -4, -12, 10, 11, 9, 18, 23, 15, 0],
            [0, 15, 23, 18, 9, 11, 10, -12, -4, -1, -8, -6, -20],
            [23, 18, 15, 11, 10, 9, 0, -1, -4, -6, -8, -12, -20],
            [18, 23, 10, 11, 9, 15, -1, -6, -8, -4, -20, -12, 0],
        ]
        for traversal, result in zip(TRAVERSALS, expected):
            with self.subTest(traversal=traversal.__name__):
                self.assertEqual(traversal(root), result)
        self.assertEqual(root.right.left.right.left.value, 10)
        self.assertTrue(is_valid_bst(root))

    def test_violation_four_edges_from_root(self):
        root = build_bst([0, -10, 20, 10, 5, 15, 30]).root
        root.right.left.left.left = Node(-1)
        self.assertLess(-1, root.right.left.left.value)
        self.assertFalse(is_valid_bst(root))
        root.right.left.left.left.value = 1
        self.assertTrue(is_valid_bst(root))

    def test_root_balance_hides_right_subtree_imbalance(self):
        root = build_bst([10, 4, 20, 2, 6, 15, 25, 1, 3, 7, 30, 35]).root

        def actual_height(node):
            if node is None:
                return 0
            return 1 + max(actual_height(node.left), actual_height(node.right))

        self.assertEqual(actual_height(root.left), 3)
        self.assertEqual(actual_height(root.right), 4)
        self.assertEqual(len(inorder(root.left)), 6)
        self.assertEqual(len(inorder(root.right)), 5)
        self.assertFalse(is_balanced(root))
        root.right.right.right.right = None
        self.assertTrue(is_balanced(root))
        self.assertEqual(actual_height(root.right), 3)


if __name__ == '__main__':
    unittest.main()
