import unittest
from basics.linked_list import LinkedList


def generate_filled_list(nums, asc=True, with_ref=True, as_str=False):
    list1 = LinkedList()

    if asc:
        if as_str:
            for n in range(nums):
                list1.insert_end(str(n))

            if with_ref:
                return list1, [str(n) for n in range(nums)]
            return list1
        else:
            for n in range(nums):
                list1.insert_end(n)

            if with_ref:
                return list1, [n for n in range(nums)]
            return list1
    else:
        if as_str:
            for n in range(nums):
                list1.insert_beginning(str(n))

            if with_ref:
                return list1, [str(n - 1) for n in range(nums, 0, -1)]
            return list1
        else:
            for n in range(nums):
                list1.insert_beginning(n)

            if with_ref:
                return list1, [n - 1 for n in range(nums, 0, -1)]
            return list1


class Test(unittest.TestCase):
    def test_len(self):
        nums = 10
        list1 = generate_filled_list(nums, with_ref=False)

        self.assertEqual(len(list1), nums)

    def test_str(self):
        nums = 10
        list1, reference_arr = generate_filled_list(nums)

        self.assertEqual(list(list1), reference_arr)

    "------------------Search------------------"
    def test_find_node(self):
        list1 = LinkedList()

        node = list1.find_node(10)
        self.assertEqual(node, None)

        nums = 10
        list1 = generate_filled_list(nums, with_ref=False, as_str=True)

        search_node = '3'
        p = list1.find_node(search_node)
        self.assertEqual(p.data, search_node)

    def test_find_node_pointer(self):
        list1 = LinkedList()

        node = list1.find_node_pointer(10)
        self.assertEqual(node, None)

        nums = 10
        list1 = generate_filled_list(nums, with_ref=False, as_str=True)

        search_node = '3'
        p = list1.find_node_pointer(search_node)
        self.assertEqual(p.next.data, search_node)

    "------------------Insert------------------"
    def test_insert_beginning(self):
        nums = 10
        list1, reference_arr = generate_filled_list(nums, asc=False)

        list_arr = list(list1)
        self.assertEqual(list_arr, reference_arr)

    def test_insert_end(self):
        nums = 10
        list1, reference_arr = generate_filled_list(nums)

        list_arr = list(list1)
        self.assertEqual(list_arr, reference_arr)

    def test_insert(self):
        insert_idx = 3
        insert_val = 100

        nums = 10
        list1, reference_arr = generate_filled_list(nums)
        list1.insert(insert_val, insert_idx)

        list_arr = list(list1)
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
        list1, reference_arr = generate_filled_list(nums)

        list1.remove_beginning()
        list_arr = list(list1)

        reference_arr = reference_arr[1:]
        self.assertEqual(list_arr, reference_arr)

    def test_remove_by_index(self):
        list1 = LinkedList()
        list1.remove_by_index(10)

        nums = 10
        list1, reference_arr = generate_filled_list(nums)

        list1.remove_by_index(100)

        list1.remove_by_index(3)
        list_arr = list(list1)

        reference_arr = reference_arr[:3] + reference_arr[4:]
        self.assertEqual(list_arr, reference_arr)

    def test_remove_by_value(self):
        list1 = LinkedList()
        list1.remove_by_value(10)

        nums = 10
        list1, reference_arr = generate_filled_list(nums, as_str=True)

        list1.remove_by_value('100')

        list1.remove_by_value('3')
        list_arr = list(list1)

        reference_arr = reference_arr[:3] + reference_arr[4:]
        self.assertEqual(list_arr, reference_arr)


if __name__ == '__main__':
    unittest.main()
