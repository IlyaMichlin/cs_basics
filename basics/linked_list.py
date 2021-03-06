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
        p = self.head
        count = 0
        while p is not None:
            p = p.next
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
        p = self.head
        for _ in range(list_len):
            yield p.data
            p = p.next

    "------------------Print------------------"
    def print_list(self):
        """
        print all nodes data
        """
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

    "------------------Search------------------"
    def find_node(self, data):
        """
        find node containing data
        :param data: value to search
        :return: node containing the data
        """
        if self.head is None:
            return

        p = self.head
        while p.data != data:
            if p.next is None:
                return
            p = p.next
        return p

    def find_node_pointer(self, data):
        """
        find node pointing to node containing data
        :param data: value to search
        :return: node pointing to node containing the data
        """
        if self.head is None:
            return

        p = self.head
        while p.next.data != data:
            p = p.next
            if p.next is None:
                return
        return p

    "------------------Insert------------------"
    def insert_beginning(self, data):
        """
        insert node at the beginning of the list
        :param data: new node value
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        """
        insert node at the end of the list
        :param data: new node value
        """
        if self.head is None:
            self.insert_beginning(data)
            return

        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(data)

    def insert(self, data, idx):
        """
        insert node at a specific index in the list
        :param idx: index of insertion
        :param data: new node value
        """
        if idx == 0:
            self.insert_beginning(data)
            return

        if self.head is None:
            return

        p = self.head
        for i in range(idx - 1):
            p = p.next
            if p is None:
                return

        if p.next is None:
            p.next = Node(data)
        else:
            node = Node(data)
            tmp = p.next
            p.next = node
            node.next = tmp

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

        p = self.head
        for _ in range(idx - 1):
            p = p.next
            if p.next is None:
                return
        remove_next(p)

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

        p = self.find_node_pointer(data)
        remove_next(p)
