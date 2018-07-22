"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and 
deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
        def __init__(self, val, left=None, right=None):
                self.val = val
                        self.left = left
                                self.right = right
                                The following test should pass:

                                node = Node('root', Node('left', Node('left.left')), Node('right'))
                                assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    #def __repr__(self):
    #    return "Node: left=%s right=%s" % (self.left.val, self.right.val)



node = Node('root', Node('left', Node('left.left')), Node('right'))
print(node)
def serialize(node):
    serialized = node.val
    if(node.left != None):
        serialized = serialized + " " + serialize(node.left)
    else:
        serialized = serialized + " " + "None"
    if(node.right != None):
        serialized = serialized + " " + serialize(node.right)
    else:
        serialized = serialized + " " + "None"

    return serialized


def deserialize(serializedTree):
    nodes = serializedTree.split(" ")
    print(nodes)
    stack = []
    
    for node in nodes:
        if(node == "None"):
            pass


    
print(serialize(node))
deserialize(serialize(node))

