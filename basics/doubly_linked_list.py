from basics.linked_list import LinkedList, Node


class DolbyNode(Node):
    def __init__(self):
        super().__init__()
        self.prev = None


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()


dlist = DoublyLinkedList()
dnode = DolbyNode()
