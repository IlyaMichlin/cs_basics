import unittest
from basics.stack import Stack


class Test(unittest.TestCase):
    def test_len(self):
        """
        test __len__()
        """
        stack_size = 10
        stack = Stack(stack_size)
        self.assertEqual(len(stack), stack_size)

    def test_simple(self):
        """
        test push(), pop(), peek()
        """
        stack_size = 10
        stack = Stack(stack_size)
        n = 0
        stack.push(n)
        peek = stack.peek()
        self.assertEqual(peek, n)
        pop = stack.pop()
        self.assertEqual(pop, n)

    def test_zero_stack(self):
        """
        test zero stack operation
        """
        stack = Stack(0)
        stack.push(0)
        pop = stack.pop()
        self.assertEqual(pop, None)

    def test_empty(self):
        """
        test empty stack operation
        """
        stack_size = 10
        stack = Stack(stack_size)

        n = 0
        stack.push(n)
        pop = stack.pop()
        self.assertEqual(pop, n)
        pop = stack.pop()
        self.assertEqual(pop, None)

    def test_full(self):
        """
        test full stack operation
        """
        stack_size = 10
        stack = Stack(stack_size)

        for n in range(stack_size + 1):
            stack.push(n)
        top = stack.top
        self.assertEqual(top, stack_size)
        peek = stack.peek()
        self.assertEqual(peek, stack_size - 1)


if __name__ == '__main__':
    unittest.main()
