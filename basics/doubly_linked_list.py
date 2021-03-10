from basics.linked_list import LinkedList, Node


class DolbyNode(Node):
    def __init__(self, data=None):
        super().__init__(data=data)
        self.prev = None


def remove_node(node):
    if node is not None:
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        del node


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    "------------------Insert------------------"
    def insert_beginning(self, new_node):
        """
        insert node at the beginning of the list
        :param new_node: new node
        """
        super().insert_beginning(new_node)
        if new_node.next is not None:
            new_node.next.prev = new_node

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
        new_node.prev = node

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

        if node.next is not None:
            tmp = node.next
            new_node.next = tmp
            tmp.prev = new_node
        node.next = new_node
        new_node.prev = node

    "------------------Remove------------------"
    def remove_beginning(self):
        """
        remove node from the beginning of the list
        """
        if self.head is None:
            return
        super().remove_beginning()
        self.head.next.prev = self.head
        self.head.prev = None

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
        for i in range(idx):
            if node.next is None:
                return
            node = node.next
        remove_node(node)

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

        node = super().find_node(data)
        remove_node(node)
