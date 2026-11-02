from homework_5.tracer import solution


def test_recursive_trace():
    @solution.tracer
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    lines = []
    solution.print = lines.append
    try:
        assert factorial(2) == 2
        assert lines == [
            "-> factorial(2)",
            "  -> factorial(1)",
            "    -> factorial(0)",
            "    <- factorial(0) = 1",
            "  <- factorial(1) = 1",
            "<- factorial(2) = 2",
        ]
        assert factorial.__name__ == "factorial"
    finally:
        del solution.print


def test_keyword_and_none():
    @solution.tracer
    def echo(value=None):
        return value

    lines = []
    solution.print = lines.append
    try:
        assert echo(value=None) is None
        assert lines == [
            "-> echo(value=None)",
            "<- echo(value=None) = None",
        ]
    finally:
        del solution.print


def test_exception_restores_depth():
    @solution.tracer
    def countdown(n):
        if n < 0:
            raise ValueError("negative")
        return countdown(n - 1)

    lines = []
    solution.print = lines.append
    try:
        raised = False
        try:
            countdown(1)
        except ValueError as error:
            raised = True
            assert str(error) == "negative"
        assert raised
        assert lines == [
            "-> countdown(1)",
            "  -> countdown(0)",
            "    -> countdown(-1)",
            "    !! countdown(-1): negative",
            "  !! countdown(0): negative",
            "!! countdown(1): negative",
        ]
        lines.clear()
        try:
            countdown(-1)
        except ValueError:
            pass
        assert lines[0] == "-> countdown(-1)"
    finally:
        del solution.print


def test_repeated_calls_and_arguments():
    @solution.tracer
    def add(first, second):
        return first + second

    lines = []
    solution.print = lines.append
    try:
        assert add(2, second=3) == 5
        assert add(-1, 1) == 0
        assert lines[0] == "-> add(2, second=3)"
        assert lines[2] == "-> add(-1, 1)"
    finally:
        del solution.print


def test_nested_list_visualization():
    @solution.tracer
    def nested_sum(item):
        if isinstance(item, int):
            return item
        total = 0
        for child in item:
            total += nested_sum(child)
        return total

    lines = []
    solution.print = lines.append
    try:
        assert nested_sum([4, [-2, [], [7, -3]], 0]) == 6
        assert lines == [
            '-> nested_sum([4, [-2, [], [7, -3]], 0])',
            '  -> nested_sum(4)',
            '  <- nested_sum(4) = 4',
            '  -> nested_sum([-2, [], [7, -3]])',
            '    -> nested_sum(-2)',
            '    <- nested_sum(-2) = -2',
            '    -> nested_sum([])',
            '    <- nested_sum([]) = 0',
            '    -> nested_sum([7, -3])',
            '      -> nested_sum(7)',
            '      <- nested_sum(7) = 7',
            '      -> nested_sum(-3)',
            '      <- nested_sum(-3) = -3',
            '    <- nested_sum([7, -3]) = 4',
            '  <- nested_sum([-2, [], [7, -3]]) = 2',
            '  -> nested_sum(0)',
            '  <- nested_sum(0) = 0',
            '<- nested_sum([4, [-2, [], [7, -3]], 0]) = 6',
        ]
    finally:
        del solution.print


def run_tests():
    tests = [
        test_recursive_trace,
        test_keyword_and_none,
        test_exception_restores_depth,
        test_repeated_calls_and_arguments,
        test_nested_list_visualization,
    ]
    for test in tests:
        test()
    print(f"Tracer: пройдено {len(tests)} тестов")
    return len(tests)


if __name__ == "__main__":
    run_tests()
