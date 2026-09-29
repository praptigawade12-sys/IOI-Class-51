class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def size(root):
    if root is None:
        return 0

    return 1+size(root.left)+size(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print("Size of binary tree:",size(root))