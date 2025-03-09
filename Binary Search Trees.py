# Binary Search Trees
# A binary search tree is a binary tree that satisfies the following property:
# For every node n, all nodes in n's left subtree have a value less than n, and all nodes in n's right subtree have a value greater than n. such that: left.data < n.data < right.data

# Graph
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(20)
n9 = TreeNode(9)
n3 = TreeNode(3)
n14 = TreeNode(14)
n12 = TreeNode(12)
n17 = TreeNode(17)
n35 = TreeNode(35)
n46 = TreeNode(46)
n28 = TreeNode(28)
n31 = TreeNode(31)
n25 = TreeNode(25)
n27 = TreeNode(27)
n23 = TreeNode(23)

root.left = n9
root.right = n35
n9.left = n3
n9.right = n14
n14.left = n12
n14.right = n17
n35.right = n46
n46.left = n28
n28.left = n25
n28.right = n31
n25.right = n27
n25.left = n23

# To make sure the tree is correct
def InOrderTraversal(node):
    if node is None:
        return
    InOrderTraversal(node.left)
    print(node.data, end=", ")
    InOrderTraversal(node.right)

# Search
def search(node,target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif node.data < target:
        return search(node.right,target)
    else:
        return search(node.left,target)

# Insert
def insert(node, data):
    if node is None:
        return TreeNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

# Find the minimum value
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Delete
def delete(node, data):
    if node is None:
        return node 
    
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Node with only one child or no child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # Node with two children: Get the inorder successor (smallest in the right subtree)
        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)
    return node
    

# Search value
result = search(root, 59)
if result is not None:
    print(f"Found: {result.data}")
else:
    print("Not found")


# Evaluate
# 1. Insert 10, insert 15, delete 20.
# 2. Insert 10, delete 20, insert 15.
# 3. Delete 35, delete 28, insert 35.

InOrderTraversal(root)