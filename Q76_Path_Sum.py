'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return None

        def dfs(node, currSum):
            if not node:
                return False
            currSum += node.val

            # means if the node has no left and right subtree(means if it is a leaf node) and if we reach to a leaf node
            # then check if our currSum is equals targetSum
            if not node.left and not node.right:
                return currSum == targetSum

            return dfs(node.left, currSum) or dfs(node.right, currSum)

        return dfs(root, 0)

# Creating a simple binary tree
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \      \
#  7    2      1
tree = TreeNode(5)
tree.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
tree.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))

obj = Solution()
obj.hasPathSum(tree, 22)

print(obj.hasPathSum(tree, 22))

