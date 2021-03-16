import unittest
from basics.circular_linked_list import CircularLinkedList
from basics.doubly_linked_list import DolbyNode
from unit_tests.universal import generate_filled_list


def get_data_from_last_to_first(last_node):
    """
    read and return data in list from last node to first
    :param last_node: last node in list
    :return: data from last node to first
    """
    node = last_node.prev
    data = [last_node.data]
    while node != last_node:
        data += [node.data]
        node = node.prev

    return data


class Test(unittest.TestCase):
    "------------------Insert------------------"
    def test_insert_beginning(self):
        """
        test insert_beginning()
        """
        # test insert on empty linked list
        list1 = CircularLinkedList()
        data = 10
        idx = 10
        list1.insert(DolbyNode(data), idx)
        self.assertEqual(list(list1), [])

        # generate linked list
        list1 = CircularLinkedList()
        list1.insert(DolbyNode(10), 0)
        list1.insert(DolbyNode(20), 1)
        list1.insert(DolbyNode(30), 1)
        reference_arr = [10, 30, 20]

        # test insert
        list_arr = list(list1)
        self.assertEqual(list_arr, reference_arr)

        # test list from last to first
        data = get_data_from_last_to_first(list1.fild_last_node())
        self.assertEqual(data, reference_arr[::-1])


    def test_insert_end(self):
        """
        test insert_end()
        """
        # test insert_end on empty linked list
        list1 = CircularLinkedList()
        data = 10
        list1.insert_end(DolbyNode(data))
        self.assertEqual(list(list1), [data])

        # generate linked list using insert_end
        nums = 10
        list1, reference_arr = generate_filled_list(CircularLinkedList, nums)
        list_arr = list(list1)
        self.assertEqual(list_arr, reference_arr)

        # test list from last to first
        data = get_data_from_last_to_first(list1.fild_last_node())
        self.assertEqual(data, reference_arr[::-1])

    def test_insert(self):
        """
        test insert()
        """
        # test on empty linked list
        list1 = CircularLinkedList()
        list1.insert(DolbyNode(10), 3)
        list_arr = list(list1)
        self.assertEqual(list_arr, [])

        # test on linked list with 1 node
        list1.insert(DolbyNode(20), 0)
        list1.insert(DolbyNode(30), 3)
        list_arr = list(list1)
        self.assertEqual(list_arr, [20, 30])

        # generate linked list
        nums = 10
        list1, reference_arr = generate_filled_list(CircularLinkedList, nums)

        # insert in the middle
        insert_idx = 3
        insert_val = 100
        list1.insert(DolbyNode(insert_val), insert_idx)

        # compare to reference
        list_arr = list(list1)
        reference_arr = reference_arr[:insert_idx] + [insert_val] + reference_arr[insert_idx:]
        self.assertEqual(list_arr, reference_arr)

        # test list from last to first
        data = get_data_from_last_to_first(list1.fild_last_node())
        self.assertEqual(data, reference_arr[::-1])

    "------------------Generic------------------"
    def test_len(self):
        """
        test __len__()
        """
        # test on empty linked list
        list1 = CircularLinkedList()
        self.assertEqual(len(list1), 0)

        # test on linked list with 1 node
        list1 = CircularLinkedList()
        list1.insert_end(DolbyNode(1))
        self.assertEqual(len(list1), 1)

        # generate linked list
        nums = 10
        list1 = generate_filled_list(CircularLinkedList, nums, with_ref=False)

        # test len()
        self.assertEqual(len(list1), nums)

    def test_str(self):
        """
        test __str__()
        """
        # generate linked list
        nums = 10
        list1, reference_arr = generate_filled_list(CircularLinkedList, nums)

        # test list()
        self.assertEqual(list(list1), reference_arr)

    "------------------Search------------------"
    def test_find_node(self):
        """
        test find_node()
        """
        # test search on empty linked list
        list1 = CircularLinkedList()
        node = list1.find_node(10)
        self.assertEqual(node, None)

        # generate linked list
        nums = 10
        list1 = generate_filled_list(CircularLinkedList, nums, with_ref=False, as_str=True)

        # test search on value not in linked list
        node = list1.find_node(nums)
        self.assertEqual(node, None)

        # test search on value in the linked list
        search_node = '3'
        node = list1.find_node(search_node)
        self.assertEqual(node.data, search_node)

    def test_find_node_pointer(self):
        """
        test find_node_pointer()
        """
        # test search on empty linked list
        list1 = CircularLinkedList()
        node = list1.find_node_pointer(10)
        self.assertEqual(node, None)

        # generate linked list
        nums = 10
        list1 = generate_filled_list(CircularLinkedList, nums, with_ref=False, as_str=True)

        # test search on value not in linked list
        search_node = str(nums)
        node = list1.find_node_pointer(search_node)
        self.assertEqual(node, None)

        # test search on value in the linked list
        search_node = '3'
        node = list1.find_node_pointer(search_node)
        self.assertEqual(node.next.data, search_node)

    def test_fild_last_node(self):
        """
        test fild_last_node()
        """
        # test search on empty linked list
        list1 = CircularLinkedList()
        node = list1.fild_last_node()
        self.assertEqual(node, None)

        # generate linked list
        nums = 1
        list1 = generate_filled_list(CircularLinkedList, nums, with_ref=False)

        # test for finding last node with 1 node
        last_node = list1.fild_last_node()
        self.assertEqual(last_node.data, nums - 1)

        # generate linked list
        nums = 10
        list1 = generate_filled_list(CircularLinkedList, nums, with_ref=False)

        # test for finding last node
        last_node = list1.fild_last_node()
        self.assertEqual(last_node.data, nums - 1)

    "------------------Remove------------------"
    def test_remove_beginning(self):
        """
        test remove_beginning()
        """
        # test on empty linked list
        list1 = CircularLinkedList()
        list1.remove_beginning()
        self.assertEqual(len(list1), 0)

        # generate linked list
        nums = 10
        list1, reference_arr = generate_filled_list(CircularLinkedList, nums)

        # remove from beginning
        list1.remove_beginning()
        list_arr = list(list1)

        # compare results to reference
        reference_arr = reference_arr[1:]
        self.assertEqual(list_arr, reference_arr)

        # test list from last to first
        data = get_data_from_last_to_first(list1.fild_last_node())
        self.assertEqual(data, reference_arr[::-1])

    def test_remove_end(self):
        """
        test remove_end()
        """
        # test on empty linked list
        list1 = CircularLinkedList()
        list1.remove_end()
        self.assertEqual(len(list1), 0)

        # generate linked list
        nums = 10
        list1, reference_arr = generate_filled_list(CircularLinkedList, nums)

        # remove from beginning
        list1.remove_end()
        list_arr = list(list1)

        # compare results to reference
        reference_arr = reference_arr[:-1]
        self.assertEqual(list_arr, reference_arr)

        # test list from last to first
        data = get_data_from_last_to_first(list1.fild_last_node())
        self.assertEqual(data, reference_arr[::-1])


    def test_remove_by_index(self):
        """
        test remove_by_index()
        """
        # test on empty linked list
        list1 = CircularLinkedList()
        list1.remove_by_index(10)
        self.assertEqual(len(list1), 0)

        # generate linked list
        nums = 10
        list1, reference_arr = generate_filled_list(CircularLinkedList, nums)

        # test removing index outside of linked list
        idx = 100
        list1.remove_by_index(idx)
        list_arr = list(list1)
        del reference_arr[idx % len(reference_arr)]
        self.assertEqual(list_arr, reference_arr)

        # test remove index from middle of linked list
        list1.remove_by_index(3)
        list_arr = list(list1)
        reference_arr = reference_arr[:3] + reference_arr[4:]
        self.assertEqual(list_arr, reference_arr)

        # test list from last to first
        data = get_data_from_last_to_first(list1.fild_last_node())
        self.assertEqual(data, reference_arr[::-1])

    def test_remove_by_value(self):
        """
        test remove by value
        """
        # test on empty linked list
        list1 = CircularLinkedList()
        list1.remove_by_value(10)
        self.assertEqual(len(list1), 0)

        # generate linked list
        nums = 10
        list1, reference_arr = generate_filled_list(CircularLinkedList, nums, as_str=True)

        # test removing value not present in linked list
        list1.remove_by_value('100')
        list_arr = list(list1)
        self.assertEqual(list_arr, reference_arr)

        # test remove node containing value from middle of linked list
        list1.remove_by_value('3')
        list_arr = list(list1)
        reference_arr = reference_arr[:3] + reference_arr[4:]
        self.assertEqual(list_arr, reference_arr)

        # test list from last to first
        data = get_data_from_last_to_first(list1.fild_last_node())
        self.assertEqual(data, reference_arr[::-1])


if __name__ == '__main__':
    unittest.main()
