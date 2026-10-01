import unittest

from solution import group_anagrams


def normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


class TestGroupAnagrams(unittest.TestCase):

    def test_typical_case(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]

        result = group_anagrams(words)

        expected = [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"],
        ]

        self.assertEqual(
            normalize(result),
            normalize(expected)
        )


    def test_empty_input(self):
        self.assertEqual(
            group_anagrams([]),
            []
        )


    def test_single_word(self):
        self.assertEqual(
            group_anagrams(["abc"]),
            [["abc"]]
        )


    def test_all_words_are_anagrams(self):
        words = ["abc", "bca", "cab", "acb"]

        result = group_anagrams(words)

        self.assertEqual(
            normalize(result),
            normalize([words])
        )


    def test_no_anagrams(self):
        words = ["abc", "def", "ghi"]

        result = group_anagrams(words)

        self.assertEqual(
            normalize(result),
            normalize([["abc"], ["def"], ["ghi"]])
        )


    def test_repeated_words(self):
        words = ["abc", "abc", "bca"]

        result = group_anagrams(words)

        self.assertEqual(
            normalize(result),
            normalize([["abc", "abc", "bca"]])
        )


    def test_empty_strings(self):
        words = ["", "", "a"]

        result = group_anagrams(words)

        self.assertEqual(
            normalize(result),
            normalize([["", ""], ["a"]])
        )


    def test_different_letter_multiplicity(self):
        words = ["abb", "bab", "ab"]

        result = group_anagrams(words)

        self.assertEqual(
            normalize(result),
            normalize([["abb", "bab"], ["ab"]])
        )


if __name__ == "__main__":
    unittest.main()