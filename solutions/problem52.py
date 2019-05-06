class LRU:

    def __init__(self, n):
        self.cache = {}
        self.capacity = n
        self.size = 0
        self.used = []

    def set(self, key, value):
        self.cache[key] = value

        if self.size == self.capacity:
            least_recent = self.used.pop(0)
            self.cache.pop(k = least_recent)

        #self.used.append(key)
        self.size += 1

    def get(self, key):
        self.used.append(key)

        return self.cache[key]

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class UsedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1

        self.size += 1

    def remove_first(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0

        else:
            self.head = self.head.next
            self.size -= 1