# Benjamin Wiens
# Find Largest Value in each Tree Row (https://leetcode.com/problems/find-largest-value-in-each-tree-row/submissions/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#deque enables fast popleft()
from collections import deque
import sys
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        largest = []
        queue = deque([root])
        maximum = -sys.maxsize
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                print(node.val)
                maximum = max(node.val, maximum)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            largest.append(maximum)
            maximum = -sys.maxsize
        return largest
                
