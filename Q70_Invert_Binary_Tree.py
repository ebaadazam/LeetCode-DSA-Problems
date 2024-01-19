'''
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        # swap the children of root node
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# Creating a simple binary tree
# Original tree:
#      1
#    /   \
#    2    3
#   / \  / \
#  4   5 6  7
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)

obj = Solution()

inverted_tree = obj.invertTree(tree)

# Printing the inverted tree (In-order traversal)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=' ')
        inorder_traversal(node.right)

inorder_traversal(inverted_tree)