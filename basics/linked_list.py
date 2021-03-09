class Node:
    def __init__(self, data=None):
        """
        linked list node
        :param data: Node data
        """
        self.data = data
        self.next = None


def remove_next(node):
    """
    remove Node the node is pointing on
    :param node: Node pointing to the Node for removal
    :return:
    """
    if node is None or node.next is None:
        return
    tmp = node.next
    node.next = tmp.next
    del tmp


class LinkedList:
    def __init__(self):
        """
        linked list
        """
        self.head = None

    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def __str__(self):
        """
        convert linked list to list and return as string
        :return: linked list as string
        """
        return str(list(self))

    def __iter__(self):
        list_len = self.__len__()
        node = self.head
        for _ in range(list_len):
            yield node.data
            node = node.next

    "------------------Print------------------"
    def print_list(self):
        """
        print all nodes data
        """
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    "------------------Search------------------"
    def find_node(self, data):
        """
        find node containing data
        :param data: value to search
        :return: node containing the data
        """
        if self.head is None:
            return

        node = self.head
        while node.data != data:
            if node.next is None:
                return
            node = node.next
        return node

    def find_node_pointer(self, data):
        """
        find node pointing to node containing data
        :param data: value to search
        :return: node pointing to node containing the data
        """
        if self.head is None:
            return

        node = self.head
        while node.next.data != data:
            node = node.next
            if node.next is None:
                return
        return node

    "------------------Insert------------------"
    def insert_beginning(self, new_node):
        """
        insert node at the beginning of the list
        :param new_node: new node
        """
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, new_node):
        """
        insert node at the end of the list
        :param new_node: new node
        """
        if self.head is None:
            self.insert_beginning(new_node)
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def insert(self, new_node, idx):
        """
        insert node at a specific index in the list
        :param idx: index of insertion
        :param new_node: new node value
        """
        if idx == 0:
            self.insert_beginning(new_node)
            return

        if self.head is None:
            return

        node = self.head
        for i in range(idx - 1):
            node = node.next
            if node is None:
                return

        if node.next is None:
            node.next = new_node
        else:
            tmp = node.next
            node.next = new_node
            new_node.next = tmp

    "------------------Remove------------------"
    def remove_beginning(self):
        """
        remove node from the beginning of the list
        """
        if self.head is None:
            return

        tmp = self.head
        self.head = tmp.next
        del tmp

    def remove_by_index(self, idx):
        """
        remove node at a specific index in the list
        :param idx: index to remove
        """
        if idx == 0:
            self.remove_beginning()
            return

        if self.head is None:
            return

        node = self.head
        for _ in range(idx - 1):
            node = node.next
            if node.next is None:
                return
        remove_next(node)

    def remove_by_value(self, data):
        """
        remove first node containing the data from the list
        :param data: data to search
        """
        if self.head is None:
            return
        elif self.head.data == data:
            self.remove_beginning()
            return

        node = self.find_node_pointer(data)
        remove_next(node)
