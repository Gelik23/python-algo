import unittest

from solution import HashTable


class CollisionKey:

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return isinstance(other, CollisionKey) and self.value == other.value


class TestHashTable(unittest.TestCase):

    def test_put_and_get(self):
        table = HashTable()

        table.put("name", "Anna")

        self.assertEqual(table.get("name"), "Anna")


    def test_update_existing_key(self):
        table = HashTable()

        table.put("age", 20)
        table.put("age", 21)

        self.assertEqual(table.get("age"), 21)
        self.assertEqual(len(table), 1)


    def test_collision_handling(self):
        table = HashTable()

        first = CollisionKey(1)
        second = CollisionKey(2)

        table.put(first, "first")
        table.put(second, "second")

        self.assertEqual(table.get(first), "first")
        self.assertEqual(table.get(second), "second")


    def test_update_value_after_collision(self):
        table = HashTable()

        first = CollisionKey(1)
        second = CollisionKey(2)

        table.put(first, "first")
        table.put(second, "second")

        table.put(first, "new_value")

        self.assertEqual(table.get(first), "new_value")
        self.assertEqual(table.get(second), "second")
        self.assertEqual(len(table), 2)


    def test_remove_element(self):
        table = HashTable()

        table.put("a", 1)
        table.put("b", 2)

        self.assertEqual(table.remove("b"), 2)
        self.assertEqual(table.get("a"), 1)


    def test_remove_last_element(self):
        table = HashTable()

        table.put("a", 1)

        table.remove("a")

        self.assertEqual(len(table), 0)

        with self.assertRaises(KeyError):
            table.get("a")


    def test_remove_element_from_collision_chain(self):
        table = HashTable()

        first = CollisionKey(1)
        second = CollisionKey(2)

        table.put(first, "first")
        table.put(second, "second")

        table.remove(first)

        self.assertEqual(table.get(second), "second")

        with self.assertRaises(KeyError):
            table.get(first)


    def test_rehash(self):
        table = HashTable()

        for i in range(100):
            table.put(i, i)

        for i in range(100):
            self.assertEqual(table.get(i), i)


    def test_empty_table(self):
        table = HashTable()

        self.assertEqual(len(table), 0)


    def test_missing_key(self):
        table = HashTable()

        with self.assertRaises(KeyError):
            table.get("key")


    def test_different_key_types(self):
        table = HashTable()

        table.put(1, "integer")
        table.put("1", "string")
        table.put((1,), "tuple")

        self.assertEqual(table.get(1), "integer")
        self.assertEqual(table.get("1"), "string")
        self.assertEqual(table.get((1,)), "tuple")

        self.assertEqual(len(table), 3)


if __name__ == "__main__":
    unittest.main()