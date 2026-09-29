class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def sum(root):
    if root is None:
        return 0
    return sum(root.left) + sum(root.right) + root.data

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)

    total = sum(root)
    print("Sum of binary tree:",total)