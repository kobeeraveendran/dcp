'''
import queue

NULL_MARKER = '-'

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):

    if node == None:
        return NULL_MARKER

    serialized = ''

    serialized.join(node.val + '|')

    serialized.join(serialize(node.left))
    serialized.join(serialize(node.right))

    return serialized

def deserialize(string):

    nodes = string.split('|')

    node_queue = queue.Queue(len(nodes))

    for node in nodes:
        node_queue.put(node)

    root = unpack_node(node_queue)

    return root    

def unpack_node(node_queue):

    dequeued = node_queue.get()

    if dequeued != None:
        if dequeued == '|':
            return None

        node = Node(dequeued)

        node.left = unpack_node(node_queue)
        node.right = unpack_node(node_queue)

        return node

    return None


test_node = Node('root', Node('left', Node('left.left')), Node('right'))

assert deserialize(serialize(test_node)).left.left.val == 'left.left'

#print('Passed.' if deserialize(serialize(test_node)).left.left.val == 'left.left' else 'Failed.')
'''

# own solution didn't work, but here's a solution from @Benjamin Braatz at 
# https://dev.to/cwetanow/daily-coding-problem-3-73i

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return ( 'Node(' + repr(self.val) + ', '
                         + repr(self.left) + ', '
                         + repr(self.right) + ')' )

    def __eq__(self, other):
        if isinstance(other, Node):
            return ( self.val == other.val and
                     self.left == other.left and
                     self.right == other.right )
        return False

    def __hash__(self):
        return hash((self.val, self.left, self.right))

serialise = repr
deserialise = eval

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialise(serialise(node)).left.left.val == 'left.left'
assert deserialise(serialise(node)) == node
assert hash(deserialise(serialise(node))) == hash(node)