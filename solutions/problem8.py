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

    if root.left == root.right == None:
        ct += 1

    if root.left and root.right and root.left.val == root.right.val:
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

    
    if root.left:
        return noglobal_count_unival_subtrees(root.left)

    if root.right:
        return noglobal_count_unival_subtrees(root.right)
    

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))


# tc2: num_univals = 5
'''
   0
  / \
 1   0
    / \
   1   0
  / \   \
 1   1   1
'''

root2 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0, right = Node(1))))

# tc3: num_univals = 1
'''
    0
     \
      1
       \
        1
         \
          1
'''
root3 = Node(0, right = Node(1, right = Node(1, right = Node(1))))

# method 1
print('Method 1 out...')
count_unival_subtrees(root)     # expected out: 5
print(ct)
ct = 0
count_unival_subtrees(root2)    # expected out: 5
print(ct)
ct = 0
count_unival_subtrees(root3)    # expected out: 1
print(ct)

# method 2
print('Method 2 out...')
print(noglobal_count_unival_subtrees(root))     # expected out: 5
print(noglobal_count_unival_subtrees(root2))    # expected out: 5
print(noglobal_count_unival_subtrees(root3))    # expected out: 1