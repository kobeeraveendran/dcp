def evaluate(string):
    return eval(string)

# note: postorder traversal of tree gives us the order in which to evaluate the function


# binary tree node
class Node:
    
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

stack = []

def evaluate_function(root: Node):
    global stack
    evaluate_bt_function(root)
    tmp = []

    while len(stack) != 0:
        val = stack.pop(0)

        if val == '+' or val == '-' or val == '*' or val == '/':
            temp_val = eval(str(tmp[-2]) + val + str(tmp[-1]))
            tmp.pop()
            tmp.pop()
            tmp.append(temp_val)

        else:
            tmp.append(val)

    return tmp[-1]

def evaluate_bt_function(root: Node):

    if root:
        evaluate_bt_function(root.left)
        evaluate_bt_function(root.right)
        stack.append(root.val)

test1 = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))

print(evaluate_function(test1))     # expected out: 45