# based on https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

class Node:

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

pre_index = 0

def reconstruct_tree(inorder: list, preorder: list):
    tree = build_helper(inorder, preorder, 0, len(inorder) - 1)

    return tree

def build_helper(inorder: list, preorder: list, start, end):

    global pre_index

    if start > end:
        return None

    node = Node(preorder[pre_index])
    pre_index += 1

    if start == end:
        return node

    in_index = inorder_search(inorder, start, end, node.val)

    node.left = build_helper(inorder, preorder, start, in_index - 1)
    node.right = build_helper(inorder, preorder, in_index + 1, end)

    return node

def inorder_search(arr, start, end, target):

    for i in range(start, end + 1):
        if arr[i] == target:
            return i

def print_tree_inorder(tree: Node):

    if not tree:
        return

    print_tree_inorder(tree.left)
    print(tree.val)
    print_tree_inorder(tree.right)

test1_inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
test1_preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']

print_tree_inorder(reconstruct_tree(test1_inorder, test1_preorder))