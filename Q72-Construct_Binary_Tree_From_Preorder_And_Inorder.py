'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is
the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None

        root = TreeNode(preorder[0])  # the first value of the preorder is the root node
        mid = inorder.index(preorder[0])  # get the position of preorder[0] in inorder and store it in mid

        # build subtrees recursively
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

obj = Solution()

# Function to print Inorder traversal of the constructed tree
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=' ')
        inorder_traversal(node.right)
    return ''

print(inorder_traversal(obj.buildTree(preorder, inorder)))
'''
    3
   / \
  9  20
    /  \
   15   7
'''