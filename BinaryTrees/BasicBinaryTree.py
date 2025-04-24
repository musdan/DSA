# Basic (most simple) implementation of a Binary search tree
# with all the DFS traversals


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        

def insert(root, data):
    
    if root.data is None:
        root.data = data
    
    if data < root.data:
        if root.left is None:
            root.left = Node(data)
            return
        else:
            insert(root.left, data)
    elif data > root.data:
        if root.right is None:
            root.right = Node(data)
            return
        else:
            insert(root.right, data)
    else:
        print("Error duplicate nodes not allowed..")
        return -1
        

def inorder(root):
    if root is None:
        return
    if root.left is not None:
        inorder(root.left)
    print("data: ", root.data)

def preorder(root):
    if root is None:
        return
    print("data: ", root.data)
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    if root is None:
        return
    postorder(root.right)
    postorder(root.left)
    print("data: ", root.data)
    
root = Node(10)
insert(root, 5)
insert(root, 2)
insert(root, 20)
insert(root, 15)
insert(root, 30)
insert(root, 6)

print("Inorder: ")
inorder(root)
print("\nPreorder: ")
preorder(root)
print("\nPostorder: ")
preorder(root)