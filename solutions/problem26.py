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

list1 = Node(1)
list1.add(Node(3)).add(Node(7)).add(Node(8)).add(Node(10))

list2 = Node(7)
list2.add(Node(8)).add(Node(1)).add(Node(10)).add(Node(13)).add(Node(7))

list3 = Node(1)
list3.add(Node(2)).add(Node(3)).add(Node(4)).add(Node(5)).add(Node(6))

def print_linked_list(head: Node):

    while head != None:
        print('{0} -> '.format(head.value), end = '')
        head = head.next

    print('Null')


# expected outputs should be obvious by viewing output
print('TEST CASE 1:')
print('Before:')
print_linked_list(list1)
print('After removing 3rd last element (0-indexed):')
print_linked_list(remove_kth_element(list1, k = 3))

print('\nTEST CASE 2:')
print('Before:')
print_linked_list(list2)
print('After removing absolute last element (k = 0):')
print_linked_list(remove_kth_element(list2, k = 0))

print('\nTEST CASE 3:')
print('Before:')
print_linked_list(list3)
print('After removing the very first element (k = list_len - 1):')
print_linked_list(remove_kth_element(list3, k = 5))