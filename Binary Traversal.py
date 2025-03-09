# Graph
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15
node7.left = node3
node7.right = node8
node15.left = node14
node15.right = node19
node19.left = node18

# Traverse
# Pre-order traversal
def PreOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    PreOrderTraversal(node.left)
    PreOrderTraversal(node.right)

# In-order traversal
def InOrderTraversal(node):
    if node is None:
        return
    InOrderTraversal(node.left)
    print(node.data, end=", ")
    InOrderTraversal(node.right)

# Post-order traversal
def PostOrderTraversal(node):
    if node is None:
        return
    PostOrderTraversal(node.left)
    PostOrderTraversal(node.right)
    print(node.data, end=", ")

PostOrderTraversal(root)
