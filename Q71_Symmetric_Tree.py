'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        # we have made another dfs() function as we need left and right parameters
        def dfs(left, right):

            # if left and right are empty
            if not left and not right:
                return True

            # if only one of them is empty
            if not left or not right:
                return False

            return (left.val == right.val) and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)


# Creating a symmetric binary tree
#        1
#       / \
#      2   2
#     / \ / \
#    3  4 4  3
symmetric_tree = TreeNode(1)
symmetric_tree.left = TreeNode(2, TreeNode(3), TreeNode(4))
symmetric_tree.right = TreeNode(2, TreeNode(4), TreeNode(3))

obj = Solution()
print(obj.isSymmetric(symmetric_tree))