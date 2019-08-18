# Benjamin Wiens
# Maximum Depth of N-Ary Tree (https://leetcode.com/problems/maximum-depth-of-n-ary-tree)

"""
Definition for a Node.
class Node:i
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.children:
                    queue.extend(node.children)
        return level
