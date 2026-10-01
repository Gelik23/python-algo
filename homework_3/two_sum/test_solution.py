import unittest

from solution import two_sum


class TestTwoSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(
            two_sum([1, 3, 4, 6], 7),
            [1, 2]
        )


    def test_answer_at_start(self):
        self.assertEqual(
            two_sum([2, 7, 11, 15], 9),
            [0, 1]
        )


    def test_negative_numbers(self):
        self.assertEqual(
            two_sum([-3, 4, 3, 90], 0),
            [0, 2]
        )


    def test_duplicate_values(self):
        self.assertEqual(
            two_sum([3, 3], 6),
            [0, 1]
        )


    def test_zeroes(self):
        self.assertEqual(
            two_sum([0, 4, 3, 0], 0),
            [0, 3]
        )


    def test_no_solution(self):
        self.assertIsNone(
            two_sum([1, 2, 3], 100)
        )


    def test_empty_list(self):
        self.assertIsNone(
            two_sum([], 10)
        )


    def test_single_element(self):
        self.assertIsNone(
            two_sum([5], 10)
        )


    def test_pair_with_negative_target(self):
        self.assertEqual(
            two_sum([-5, -2, 4, 7], -7),
            [0, 1]
        )


    def test_additional_cases(self):
        test_cases = [
            ([5, 1, 8, 2], 10, [2, 3]),
            ([10, -10, 20, 30], 0, [0, 1]),
            ([1, 5, 3, 7], 8, [1, 2]),
        ]

        for nums, k, expected in test_cases:
            with self.subTest(nums=nums, k=k):
                self.assertEqual(
                    two_sum(nums, k),
                    expected
                )


if __name__ == "__main__":
    unittest.main()