from basics.doubly_linked_list import DoublyLinkedList


def insert_node(node, new_node):
    """
    insert new node after node
    :param node: node in the circular linked list
    :param new_node: new node to insert
    """
    new_node.prev = node
    new_node.next = node.next
    node.next.prev = new_node
    node.next = new_node


def remove_node(node, head):
    """
    remove node from circular linked list
    :param node: node to remove
    """
    if head == node:
        head = node.next
    if node.next == node:
        head = None
    node.next.prev = node.prev
    node.prev.next = node.next
    del node

    return head


class CircularLinkedList(DoublyLinkedList):
    def __len__(self):
        if self.head is None:
            return 0
        elif self.head.next == self.head:
            return 1

        node = self.head.next
        count = 1
        while node != self.head:
            node = node.next
            count += 1
        return count

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
            node = node.next
            if node == self.head:
                return
        return node

    def find_node_pointer(self, data):
        """
        find node pointing to node containing data
        :param data: value to search
        :return: node pointing to node containing the data
        """
        if self.head is None:
            return

        node = self.find_node(data)
        if node is None:
            return None
        return node.prev

    def fild_last_node(self):
        """
        find and return the last node in the list
        :return: last node in the list
        """
        if self.head is None:
            return

        return self.head.prev

    "------------------Insert------------------"
    def insert_beginning(self, new_node):
        """
        insert node at the beginning of the list
        :param new_node: new node
        """
        new_node.next = self.head
        self.head = new_node
        if new_node.next is None:
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = new_node.next.prev
            new_node.next.prev.next = new_node
            new_node.next.prev = new_node

    def insert_end(self, new_node):
        """
        insert node at the end of the list
        :param new_node: new node
        """
        if self.head is None:
            self.insert_beginning(new_node)
            return

        insert_node(self.head.prev, new_node)

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

        insert_node(node, new_node)

    "------------------Remove------------------"
    def remove_beginning(self):
        """
        remove node from the beginning of the list
        """
        if self.head is None:
            return
        elif self.head.next == self.head:
            node = self.head
            self.head = None
            del node
            return

        node = self.head
        # self.head = node.next
        self.head = remove_node(node, self.head)

    def remove_end(self):
        """
        remove node from the end of list
        """
        if self.head is None:
            return

        self.head = remove_node(self.head.prev, self.head)

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
            node = node.next
        self.head = remove_node(node, self.head)

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

        node = self.find_node(data)
        if node is None:
            return
        self.head = remove_node(node, self.head)
