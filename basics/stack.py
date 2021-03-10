class Stack:
    """
    stack implemented using arrays
    """
    def __init__(self, size):
        self.stack = [None] * size
        self.top = 0
        self.is_empty = True
        if size < 1:
            self.is_full = True
        else:
            self.is_full = False

    def __len__(self):
        return len(self.stack)

    def push(self, data):
        """
        push operation
        :param data: data to push
        """
        if self.is_full:
            return

        self.stack[self.top] = data
        self.top += 1

        self.is_empty = False
        if self.top == len(self.stack):
            self.is_full = True

    def pop(self):
        """
        pop operation
        :return: top value
        """
        if self.is_empty:
            return None

        p = self.stack[self.top - 1]
        self.top -= 1

        self.is_full = False
        if self.top == 0:
            self.is_empty = True

        return p

    def peek(self):
        """
        return top value without removing
        :return: top value
        """
        if self.is_empty:
            return None
        return self.stack[self.top - 1]
