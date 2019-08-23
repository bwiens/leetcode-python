# Benjamin Wiens
# Maximum Level Sum of a Binary Tree (https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque([root])
        max_level, current_level = 1, 1
        level_sum, maximum = root.val, root.val
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > maximum:
                max_level = current_level
                maximum = level_sum
            current_level += 1
            level_sum = 0
        return max_level
