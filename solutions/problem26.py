class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def add(self, node):
        self.next = node
        return node

def remove_kth_element(linked_list, k):
    count = -1

    head = linked_list

    # once count reaches k, start keeping track of the LL element k iterations before it (aka the head at first)
    prev = None
    rewind = linked_list
    after = linked_list.next

    while linked_list != None:

        if count >= k:
            prev = rewind
            rewind = after
            after = after.next

        linked_list = linked_list.next
        count += 1

    if prev != None:
        prev.next = after

    else:
        head = after

    return head

test1 = Node(1)
test1.add(Node(3)).add(Node(7)).add(Node(8)).add(Node(10))

def print_linked_list(head: Node):

    while head != None:
        print('{0} -> '.format(head.value), end = '')
        head = head.next

    print('Null')

print('TEST CASE 1:')
print('Before:')
print_linked_list(test1)
print('After:')
print_linked_list(remove_kth_element(test1, k = 3))