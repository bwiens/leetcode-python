# Benjamin Wiens
# Maximum Depth of Binary Tree (https://leetcode.com/problems/maximum-depth-of-binary-tree)# BFS Solution
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level
