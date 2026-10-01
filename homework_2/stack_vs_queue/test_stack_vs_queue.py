import unittest

from .stack_vs_queue import Queue, Stack


class TestStack(unittest.TestCase):
    def test_stack_uses_lifo_order(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.peek(), 30)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.empty())

    def test_stack_after_removing_and_adding_elements(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 1)

    def test_stack_visualization_example(self):
        stack = Stack()

        stack.push(4)
        stack.push(7)
        self.assertEqual(stack.pop(), 7)
        stack.push(9)

        self.assertEqual(stack.peek(), 9)
        self.assertEqual(stack.pop(), 9)
        self.assertEqual(stack.pop(), 4)
        self.assertTrue(stack.empty())

    def test_empty_stack_returns_none(self):
        stack = Stack()

        self.assertTrue(stack.empty())
        self.assertIsNone(stack.pop())
        self.assertIsNone(stack.peek())

    def test_stack_with_one_element(self):
        stack = Stack()

        stack.push(42)

        self.assertFalse(stack.empty())
        self.assertEqual(stack.peek(), 42)
        self.assertEqual(stack.pop(), 42)
        self.assertTrue(stack.empty())
        self.assertIsNone(stack.head)

    def test_stack_supports_duplicate_values(self):
        stack = Stack()

        stack.push(5)
        stack.push(5)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 5)

    def test_stack_can_be_used_again_after_becoming_empty(self):
        stack = Stack()

        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        stack.push(2)

        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertTrue(stack.empty())


class TestQueue(unittest.TestCase):
    def test_queue_uses_fifo_order(self):
        queue = Queue()

        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)
        self.assertTrue(queue.empty())

    def test_queue_after_becoming_empty_can_be_used_again(self):
        queue = Queue()

        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(2)

        self.assertEqual(queue.peek(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertTrue(queue.empty())

    def test_queue_visualization_example(self):
        queue = Queue()

        queue.enqueue(4)
        queue.enqueue(7)
        self.assertEqual(queue.dequeue(), 4)
        queue.enqueue(9)

        self.assertEqual(queue.peek(), 7)
        self.assertEqual(queue.dequeue(), 7)
        self.assertEqual(queue.dequeue(), 9)
        self.assertTrue(queue.empty())

    def test_empty_queue_returns_none(self):
        queue = Queue()

        self.assertTrue(queue.empty())
        self.assertIsNone(queue.dequeue())
        self.assertIsNone(queue.peek())

    def test_queue_with_one_element_clears_both_links(self):
        queue = Queue()

        queue.enqueue(42)

        self.assertFalse(queue.empty())
        self.assertEqual(queue.peek(), 42)
        self.assertEqual(queue.dequeue(), 42)
        self.assertTrue(queue.empty())
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_queue_supports_duplicate_values(self):
        queue = Queue()

        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(3)

        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 3)


if __name__ == "__main__":
    unittest.main()
