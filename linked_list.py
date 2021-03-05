class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next


list1 = LinkedList()
list1.head = Node('h')
list1.head.next = Node('hh')
list1.head.next.next = Node('hhh')

list1.print_list()
