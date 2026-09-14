import unittest

from .even_sum import max_even_sum


class TestMaxEvenSum(unittest.TestCase):
    def test_different_arrays(self):
        cases = [
            ([5, 7, 13, 2, 14], 36),
            ([3], 0),
            ([2], 2),
            ([2, 4, 6], 12),
            ([1, 2, 3], 6),
            ([1, 2, 2], 4),
            ([9, 5, 7], 16),
            ([], 0),
        ]

        for numbers, expected in cases:
            with self.subTest(numbers=numbers):
                self.assertEqual(max_even_sum(numbers), expected)

if __name__ == "__main__":
    unittest.main()
