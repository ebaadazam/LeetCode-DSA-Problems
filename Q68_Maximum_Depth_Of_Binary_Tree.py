'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
'''

# THIS CAN BE DONE IN 3 WAYS- DFS Recursive, DFS Iterative, BFS Iterative

# DFS Recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)

obj = Solution()
print("Maximum Depth:", obj.maxDepth(tree))


# DFS Iterative
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        stack = [[root, 1]]  # stack containing the node and depth
        res = 0
        while stack:
            node, depth = stack.pop() #keep popping the node and its depth and replace it with its child nodes
            if node:
                res = max(res, depth)  # store the max depth so far in it
                stack.append([node.left, depth+1]) #append left subtree
                stack.append([node.right, depth+1]) #append right subtree
        return res  #return the max depth stored in res

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)

obj = Solution()
print("Maximum Depth:", obj.maxDepth(tree))




# BFS Iterative

# deque (double-ended queue) is a DS provided by Python collections module that allows you to efficiently append and pop
# elements from both ends of the queue. It is useful where you need fast and O(1) time complexity for adding or removing
# elements from both the front and the back of the queue. A deque is employed to maintain the order of the nodes at each
# level in this BFS approach.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)

obj = Solution()
print("Maximum Depth:", obj.maxDepth(tree))







