class Queue:

    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, value):
        self.in_stack.push(value)
        self.out_stack.stack.insert(0, value)

    def dequeue(self):
        self.in_stack.stack.pop(0)
        return self.out_stack.pop()

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()