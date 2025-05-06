
"""" Most simplest Binary Tree code possible.."""


class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

""" Given a root Node and data, insert the data at the appropriate
node of the Binary tree
NOTE: that the root node is untouched 
return statements in a recursive function makes it more complicated
so here no return function has been used..
"""
def insert(root, data):
    if data < root.data:
        if root.left is None:
            root.left = Node(data)
        else:
            """we go left until the node is None"""
            insert(root.left, data)
    else:
        """ We know data has to go right"""
        if root.right is None:
            root.right = Node(data)
        else:
            insert(root.right, data)
    """ No need for a return here, but just for clarity"""
    return

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print("iorder data: ", root.data)
    inorder(root.right)
    
    
"""" First create a root node using the Node class.."""

root = Node(100)

""" Now use the insert function to insert subsequent nodes.."""

insert(root, 90)
insert(root, 80)
insert(root, 75)
insert(root, 77)
insert(root, 95)
insert(root, 100)

inorder(root)


