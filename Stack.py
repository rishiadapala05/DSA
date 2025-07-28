class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None
