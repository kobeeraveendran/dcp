class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.maxes = []

    def push(self, val):
        self.stack.append(val)

        if len(self.maxes) > 0:
            if val >= self.maxes[-1]:
                self.maxes.append(val)

        else:
            self.maxes.append(val)

        self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        val = self.stack.pop()

        if val == self.maxes[-1]:
            self.maxes.pop()

        self.size -= 1

        return val

    def max(self):
        if len(self.maxes) == 0:
            return None

        else:
            return self.maxes[-1]

print('\n----- TEST 1 -----\n')

test1 = Stack()
test1.push(9)
print(test1.stack)
test1.push(20)
print(test1.stack)
print('current max: ', test1.max())
test1.pop()
print(test1.stack)
print('current max: ', test1.max())

print('\n----- TEST 2 -----\n')

test2 = Stack()
test2.push(10)
print('current max: ', test2.max())
test2.push(20)
print('current max: ', test2.max())
test2.push(11)
test2.push(20)
test2.pop()
print('current max: ', test2.max())
print(test2.maxes)
print(test2.stack)