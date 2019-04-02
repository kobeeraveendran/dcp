# basic linked list node class
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

# O(M + N) time, O(M) space (could also be re-written to be O(min(M, N)) space by 
# choosing the smaller list to construct the set out of)
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

    return None

# O(M + N) time, O(1) space
def find_intersection(listA: Node, listB: Node):
    a_head = listA
    b_head = listB

    while listA.value != listB.value:
        if listA.next == None:
            listA = a_head

        elif listB.next == None:
            listB = b_head

        else:
            listA = listA.next
            listB = listB.next

    return listA


test1_a = Node(3, Node(7, Node(8, Node(10, None))))
test1_b = Node(99, Node(1, Node(8, Node(10, None))))

test2_a = Node(8, Node(10, None))
test2_b = Node(3, Node(7, Node(8, Node(10, None))))

test3_a = Node(2, Node(8, Node(10, None)))
test3_b = Node(3, Node(7, Node(8, Node(10, None))))

print(find_intersection_linear_space(test1_a, test1_b).value)
print(find_intersection(test1_a, test1_b).value)

print(find_intersection_linear_space(test2_a, test2_b).value)
print(find_intersection(test2_a, test2_b).value)

print(find_intersection_linear_space(test3_a, test3_b).value)
print(find_intersection(test3_a, test3_b).value)