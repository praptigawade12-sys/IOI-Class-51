class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def size(root):
    if root is None:
        return 0

    stack = [root]
    count = 0

    while stack:
        node = stack.pop()
        count += 1

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return count

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print("Size of binary tree:",size(root))