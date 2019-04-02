# basic linked list node class
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

def find_intersection_linear_space(listA: Node, listB: Node):
    seen = set()

    # iterate through A
    while listA.next != None:
        seen.add(listA.value)
        listA = listA.next

    # iterate through B
    while listB.next != None:
        if listB.value in seen:
            return listB
        
        listB = listB.next

list_A = Node(3, Node(7, Node(8, Node(10, None))))
list_B = Node(99, Node(1, Node(8, Node(10, None))))

print(find_intersection_linear_space(list_A, list_B).value)