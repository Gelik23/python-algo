from homework_5.permutations.solution import permutations
from homework_5.tracer import solution as tracer_module


def test_examples():
    assert permutations([1, 2, 3]) == [
        [1, 2, 3], [1, 3, 2], [2, 1, 3],
        [2, 3, 1], [3, 1, 2], [3, 2, 1],
    ]
    assert permutations([0, 1]) == [[0, 1], [1, 0]]
    assert permutations([1]) == [[1]]


def test_empty():
    assert permutations([]) == [[]]


def test_duplicates_and_negative():
    assert permutations([2, -1, 2]) == [
        [2, 2, -1], [2, -1, 2], [-1, 2, 2],
    ]


def test_all_equal():
    assert permutations([5, 5, 5]) == [[5, 5, 5]]


def test_input_and_results_are_independent():
    nums = [3, 1, 2]
    result = permutations(nums)
    assert nums == [3, 1, 2]
    result[0][0] = 99
    assert result[1] == [3, 2, 1]
    assert nums == [3, 1, 2]
    assert permutations([1]) == [[1]]


def test_six_distinct_elements():
    nums = [-2, -1, 0, 1, 2, 3]
    result = permutations(nums)
    assert len(result) == 720
    assert len(set(tuple(item) for item in result)) == 720
    for item in result:
        assert sorted(item) == nums


def test_several_repeated_values():
    result = permutations([0, 0, 1, 1])
    assert len(result) == 6
    assert len(set(tuple(item) for item in result)) == 6
    for item in result:
        assert sorted(item) == [0, 0, 1, 1]


def test_four_element_visualization():
    lines = []
    tracer_module.print = lines.append
    nums = [2, -1, 2, 0]
    try:
        result = permutations(nums, trace=True)
        assert result == [
            [2, 2, -1, 0],
            [2, 2, 0, -1],
            [2, -1, 2, 0],
            [2, -1, 0, 2],
            [2, 0, 2, -1],
            [2, 0, -1, 2],
            [-1, 2, 2, 0],
            [-1, 2, 0, 2],
            [-1, 0, 2, 2],
            [0, 2, 2, -1],
            [0, 2, -1, 2],
            [0, -1, 2, 2],
        ]
        assert lines[0] == "-> backtrack([])"
        assert lines[-1] == "<- backtrack([]) = 12"
        assert "  <- backtrack([2]) = 6" in lines
        assert "  <- backtrack([-1]) = 3" in lines
        assert "  <- backtrack([0]) = 3" in lines
        assert nums == [2, -1, 2, 0]
    finally:
        del tracer_module.print


def run_tests():
    tests = [
        test_examples, test_empty, test_duplicates_and_negative,
        test_all_equal, test_input_and_results_are_independent,
        test_six_distinct_elements, test_several_repeated_values,
        test_four_element_visualization,
    ]
    for test in tests:
        test()
    print(f"Permutations: пройдено {len(tests)} тестов")
    return len(tests)


if __name__ == "__main__":
    run_tests()
