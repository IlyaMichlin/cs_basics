import unittest
from basics.linked_list import LinkedList


class Test(unittest.TestCase):
    def test_len(self):
        list1 = LinkedList()

        nums = 10
        for n in range(nums):
            list1.insert_beginning(n)

        self.assertEqual(len(list1), nums)

    def test_str(self):
        list1 = LinkedList()

        nums = 10
        for n in range(nums):
            list1.insert_end(n)

        reference_arr = [n for n in range(nums)]

        self.assertEqual(list(list1), reference_arr)

    "------------------Search------------------"
    def test_find_node(self):
        list1 = LinkedList()

        node = list1.find_node(10)
        self.assertEqual(node, None)

        nums = 10
        for n in range(nums):
            list1.insert_end(str(n))

        search_node = '3'
        p = list1.find_node(search_node)
        self.assertEqual(p.data, search_node)

    def test_find_node_pointer(self):
        list1 = LinkedList()

        node = list1.find_node_pointer(10)
        self.assertEqual(node, None)

        nums = 10
        for n in range(nums):
            list1.insert_end(str(n))

        search_node = '3'
        p = list1.find_node_pointer(search_node)
        self.assertEqual(p.next.data, search_node)

    "------------------Insert------------------"
    def test_insert_beginning(self):
        list1 = LinkedList()

        nums = 10
        for n in range(nums):
            list1.insert_beginning(n)

        list_arr = list(list1)
        reference_arr = [n-1 for n in range(nums, 0, -1)]

        self.assertEqual(list_arr, reference_arr)

    def test_insert_end(self):
        list1 = LinkedList()

        nums = 10
        for n in range(nums):
            list1.insert_end(n)

        list_arr = list(list1)

        reference_arr = [n for n in range(nums)]
        self.assertEqual(list_arr, reference_arr)

    def test_insert(self):
        list1 = LinkedList()

        insert_idx = 3
        insert_val = 100

        nums = 10
        for n in range(nums):
            list1.insert_end(n)
        list1.insert(insert_val, insert_idx)

        list_arr = list(list1)
        reference_arr = [n for n in range(nums)]
        reference_arr = reference_arr[:insert_idx] + [insert_val] + reference_arr[insert_idx:]

        self.assertEqual(list_arr, reference_arr)

    def test_insert_empty(self):
        list1 = LinkedList()
        list1.insert(10, 3)

        list_arr = list(list1)

        self.assertEqual(list_arr, [])

        list1.insert(20, 0)
        list1.insert(30, 3)

        list_arr = list(list1)
        self.assertEqual(list_arr, [20])

    "------------------Remove------------------"
    def test_remove_beginning(self):
        list1 = LinkedList()
        list1.remove_beginning()

        nums = 10
        for n in range(nums):
            list1.insert_end(n)

        list1.remove_beginning()
        list_arr = list(list1)

        reference_arr = [n for n in range(nums)][1:]
        self.assertEqual(list_arr, reference_arr)

    def test_remove_by_index(self):
        list1 = LinkedList()
        list1.remove_by_index(10)

        nums = 10
        for n in range(nums):
            list1.insert_end(n)

        list1.remove_by_index(100)

        list1.remove_by_index(3)
        list_arr = list(list1)

        reference_arr = [n for n in range(nums)]
        reference_arr = reference_arr[:3] + reference_arr[4:]
        self.assertEqual(list_arr, reference_arr)

    def test_remove_by_value(self):
        list1 = LinkedList()
        list1.remove_by_value(10)

        nums = 10
        for n in range(nums):
            list1.insert_end(str(n))

        list1.remove_by_value('100')

        list1.remove_by_value('3')
        list_arr = list(list1)

        reference_arr = [str(n) for n in range(nums)]
        reference_arr = reference_arr[:3] + reference_arr[4:]
        self.assertEqual(list_arr, reference_arr)


if __name__ == '__main__':
    unittest.main()
