class Node:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_second_largest_node(root):

    while root.right != None:
        parent = root
        root = root.right

    return parent

test1 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(8)))
test2 = Node(1, right = Node(2, right = Node(3, right = Node(4, right = Node(6)))))

print(find_second_largest_node(test1).value)
print(find_second_largest_node(test2).value)