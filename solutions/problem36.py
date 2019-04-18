class Node:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# best case runtime: O(1) - when BST is a left-leaning linked list
# average; worst case runtime: O(logn) - well-formed BST; when BST is a right-leaning linked list
def find_second_largest_node(root):

    parent = root.left

    while root.right != None:
        parent = root
        root = root.right

    return parent

test1 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(8)))

# BST devolved into linked list going to the right
test2 = Node(1, right = Node(2, right = Node(3, right = Node(4, right = Node(6)))))

# BST devolved into linked list going to the left
test3 = Node(7, left = Node(5, left = Node(4, left = Node(3, left = Node(2, left = Node(1))))))

print(find_second_largest_node(test1).value)
print(find_second_largest_node(test2).value)
print(find_second_largest_node(test3).value)