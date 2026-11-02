from homework_5.AVL.solution import AVL


def check_tree(tree, expected):
    def check(node, lower=None, upper=None):
        if node is None:
            return 0
        if lower is not None:
            assert node.value > lower
        if upper is not None:
            assert node.value < upper
        left = check(node.left, lower, node.value)
        right = check(node.right, node.value, upper)
        assert abs(left - right) <= 1
        actual_height = 1 + max(left, right)
        assert node.height == actual_height
        return actual_height

    check(tree.root)
    assert tree.inorder() == sorted(expected)


def build_tree(values):
    tree = AVL()
    expected = set()
    for value in values:
        tree.insert(value)
        expected.add(value)
        check_tree(tree, expected)
    return tree


def test_empty():
    tree = AVL()
    assert tree.search(10) is False
    tree.delete(10)
    check_tree(tree, [])


def test_single():
    tree = build_tree([5])
    assert tree.search(5) is True
    tree.delete(5)
    assert tree.root is None
    check_tree(tree, [])


def test_four_rotations():
    for values in [[30, 20, 10], [10, 20, 30], [30, 10, 20], [10, 30, 20]]:
        tree = build_tree(values)
        assert tree.root.value == 20
        assert tree.root.left.value == 10
        assert tree.root.right.value == 30


def test_duplicates_negative_and_zero():
    tree = build_tree([0, -10, 10, 0, -10, 10])
    check_tree(tree, [-10, 0, 10])
    tree.delete(0)
    check_tree(tree, [-10, 10])
    assert tree.search(0) is False


def test_delete_leaf():
    tree = build_tree([20, 10, 30])
    tree.delete(10)
    check_tree(tree, [20, 30])


def test_delete_node_with_one_child():
    tree = build_tree([20, 10, 30, 25])
    tree.delete(30)
    check_tree(tree, [10, 20, 25])


def test_delete_root_with_one_child():
    for values in [[20, 10], [10, 20]]:
        tree = build_tree(values)
        tree.delete(values[0])
        check_tree(tree, [values[1]])
        assert tree.root.value == values[1]


def test_delete_two_children_and_deep_successor():
    tree = build_tree([20, 10, 40, 5, 15, 30, 50, 25, 35, 27])
    tree.delete(20)
    check_tree(tree, [5, 10, 15, 25, 27, 30, 35, 40, 50])
    assert tree.search(20) is False


def test_delete_missing():
    tree = build_tree([-10, 0, 10])
    tree.delete(100)
    tree.delete(-100)
    check_tree(tree, [-10, 0, 10])


def test_sorted_and_reverse_sorted():
    for values in [list(range(200)), list(range(199, -1, -1))]:
        tree = build_tree(values)
        expected = set(values)
        for value in values:
            assert tree.search(value) is True
            tree.delete(value)
            expected.remove(value)
            check_tree(tree, expected)
        assert tree.root is None


def test_multistep_visualization():
    values = [50, 30, 70, 10, 40, 60, 80, 20]
    tree = build_tree(values)
    tree.insert(15)
    values.append(15)
    check_tree(tree, values)
    assert tree.root.value == 50
    assert tree.root.left.left.value == 15
    assert tree.root.left.left.left.value == 10
    assert tree.root.left.left.right.value == 20
    tree.delete(50)
    values.remove(50)
    check_tree(tree, values)
    assert tree.root.value == 60
    assert tree.root.right.left is None
    tree.delete(80)
    values.remove(80)
    check_tree(tree, values)
    assert tree.root.value == 30
    assert tree.root.right.value == 60
    assert tree.root.right.left.value == 40
    assert tree.root.height == 3
    assert tree.search(40) is True
    assert tree.search(50) is False


def run_tests():
    tests = [
        test_empty, test_single, test_four_rotations,
        test_duplicates_negative_and_zero,
        test_delete_leaf, test_delete_node_with_one_child,
        test_delete_root_with_one_child,
        test_delete_two_children_and_deep_successor, test_delete_missing,
        test_sorted_and_reverse_sorted,
        test_multistep_visualization,
    ]
    for test in tests:
        test()
    print(f"AVL: пройдено {len(tests)} тестов")
    return len(tests)


if __name__ == "__main__":
    run_tests()
