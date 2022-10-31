class Node:
    def __init__ (self,data):
        self.data=data
        self.right=None
        self.left=None

root=Node(3)
root.left=Node(1)
root.right=Node(2)
root.left.right=Node(7)
root.left.left=Node(16)
print(root.left.data)
print(root.left.left.data)
print(root.left.left)
