import unittest

from .palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_different_numbers(self):
        cases = [
            (1, True),
            (7, True),
            (11, True),
            (121, True),
            (12321, True),
            (1001, True),
            (1000021, False),
            (31, False),
            (12345, False),
            (10, False),
        ]

        for number, expected in cases:
            with self.subTest(number=number):
                self.assertIs(is_palindrome(number), expected)

    def test_invalid_values(self):
        for number in [0, -121]:
            with self.subTest(number=number), self.assertRaises(ValueError):
                is_palindrome(number)


if __name__ == "__main__":
    unittest.main()
