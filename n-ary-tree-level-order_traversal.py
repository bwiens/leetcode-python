# Benjamin Wiens
# N-Ary Tree Level Order Traversal (https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        level = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(level)
            level = []
        return result
