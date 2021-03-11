from basics.linked_list import LinkedList, Node


class Queue:
    """
    Queue using Circular Double Linked List
    """
    def __init__(self):
        self.queue = LinkedList()
        self.is_full = False
        self.is_empty = True

    def __len__(self):
        return len(self.queue)

    def enqueue(self, data):
        """
        add an item to the queue
        :param data: data to add
        """
        node = Node(data)
        self.queue.insert_end(node)

    def dequeue(self):
        """
        remove an item from the queue
        :return: item data
        """
        node = self.queue.fild_last_node()
        self.queue.remove_beginning()

        if self.queue.head is None:
            self.is_empty = True
        else:
            self.is_empty = False

        if node is None:
            return None
        return node.data

    def peek(self):
        """
        gets the element at the front of the queue without removing it
        :return: item data
        """
        node = self.queue.head
        if node is None:
            return None
        return node.data
