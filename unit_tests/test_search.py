import unittest
from basics.search import search_linear, search_binary, search_interpolation


class Test(unittest.TestCase):
    def test_search_linear(self):
        """
        test search_linear()
        """
        array = [1.5 * n for n in range(10)]

        vals = [-10, 100, 3, 7.5, 8]
        idxs = [None, None, 2, 5, None]
        for val, idx in zip(vals, idxs):
            index = search_linear(array, val)
            self.assertEqual(index, idx)

    def test_search_binary(self):
        """
        test search_binary()
        """
        array = [1.5 * n for n in range(10)]

        vals = [-10, 100, 3, 7.5, 8]
        idxs = [None, None, 2, 5, None]
        for val, idx in zip(vals, idxs):
            index = search_binary(array, val)
            self.assertEqual(index, idx)

    def test_search_interpolation(self):
        """
        test search_interpolation()
        """
        array = [1.5 * n for n in range(10)]

        vals = [-10, 100, 3, 7.5, 8]
        idxs = [None, None, 2, 5, None]
        for val, idx in zip(vals, idxs):
            index = search_interpolation(array, val)
            self.assertEqual(index, idx)


if __name__ == '__main__':
    unittest.main()
