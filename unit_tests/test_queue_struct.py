import unittest
from basics.queue_struct import Queue


def generate_queue(queue_size):
    queue = Queue()

    for n in range(queue_size):
        queue.enqueue(n)

    return queue


class Test(unittest.TestCase):
    def test_len(self):
        """
        test __len__()
        """
        queue_size = 10
        queue = generate_queue(queue_size)

        self.assertEqual(len(queue), queue_size)

    def test_simple(self):
        """
        test enqueue(), dequeue(), peek()
        """
        queue = Queue()

        n = 0
        queue.enqueue(n)
        peek = queue.peek()
        self.assertEqual(peek, n)
        dequeue = queue.dequeue()
        self.assertEqual(dequeue, n)

    def test_empty(self):
        """
        test empty queue operation
        """
        queue = Queue()
        n = 0
        queue.enqueue(n)
        dequeue = queue.dequeue()
        self.assertEqual(dequeue, n)
        dequeue = queue.dequeue()
        self.assertEqual(dequeue, None)

    def test_full(self):
        """
        test full stack operation
        """
        queue_size = 10
        queue = generate_queue(queue_size)
        self.assertEqual(len(queue), queue_size)

        peek = queue.peek()
        self.assertEqual(peek, queue_size - 1)


if __name__ == '__main__':
    unittest.main()
