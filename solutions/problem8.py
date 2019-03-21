class Node(object):
    '''
    Tree Node
    If the tree rooted at this node is a unival tree, then 'is_unival' == True
    '''
    def __init__(self, val = None, left = None, right= None, is_unival = False):
        self.val = val
        self.left = left
        self.right = right
        self.is_unival = is_unival

ct = 0

def count_unival_subtrees(root):

    global ct

    if root.left == root.right == None or root.left.val == root.right.val:
        ct += 1

    if root.left:
        count_unival_subtrees(root.left)

    if root.right:
        count_unival_subtrees(root.right)

def noglobal_count_unival_subtrees(root):

    if root.left == root.right == None:
        return 1

    if root.left and root.right:
        if root.left.val == root.right.val:
            return 1 + noglobal_count_unival_subtrees(root.left) + noglobal_count_unival_subtrees(root.right)

        return noglobal_count_unival_subtrees(root.left) + noglobal_count_unival_subtrees(root.right)


root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

count_unival_subtrees(root)

# method 1
print(ct)

# method 2
print(noglobal_count_unival_subtrees(root))