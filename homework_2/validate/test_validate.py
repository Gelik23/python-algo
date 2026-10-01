import unittest

from .validate import validate_stack_sequences


class TestValidateStackSequences(unittest.TestCase):
    def test_sequence_from_first_example_is_valid(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [1, 3, 5, 4, 2]

        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_sequence_from_second_example_is_invalid(self):
        pushed = [1, 2, 3]
        popped = [3, 1, 2]

        self.assertFalse(validate_stack_sequences(pushed, popped))

    def test_elements_can_be_popped_immediately(self):
        self.assertTrue(validate_stack_sequences([1, 2, 3], [1, 2, 3]))

    def test_elements_can_be_popped_in_reverse_order(self):
        self.assertTrue(validate_stack_sequences([1, 2, 3], [3, 2, 1]))

    def test_one_element(self):
        self.assertTrue(validate_stack_sequences([42], [42]))

    def test_multiple_pops_after_one_push(self):
        pushed = [2, 5, 1, 4, 3, 6]
        popped = [1, 3, 4, 5, 6, 2]

        self.assertTrue(validate_stack_sequences(pushed, popped))

    def test_another_invalid_order(self):
        self.assertFalse(
            validate_stack_sequences([1, 2, 3, 4], [2, 4, 1, 3])
        )

    def test_maximum_length(self):
        pushed = list(range(100_000))
        popped = list(reversed(pushed))

        self.assertTrue(validate_stack_sequences(pushed, popped))


if __name__ == "__main__":
    unittest.main()
