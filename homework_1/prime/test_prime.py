import unittest

from .prime import count_primes


class TestCountPrimes(unittest.TestCase):
    def test_different_limits(self):
        cases = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 1),
            (4, 2),
            (10, 4),
            (20, 8),
            (100, 25),
        ]

        for limit, expected in cases:
            with self.subTest(limit=limit):
                self.assertEqual(count_primes(limit), expected)

if __name__ == "__main__":
    unittest.main()
