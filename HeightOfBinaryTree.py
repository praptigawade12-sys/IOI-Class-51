class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)

    h = max(left,right) + 1
    return h

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.left.left = Node(5)

print("Height of Binary Tree:",max_depth(root))