#!/usr/bin/python
# Benjamin Wiens
# Find Bottom Left Tree Value (https://leetcode.com/problems/find-bottom-left-tree-value/)

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        left_most = None
        first_in_level = True
        result = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # the first in level will always be left-most
                if first_in_level:
                    result = node.val
                first_in_level = False
            first_in_level = True
        return result
