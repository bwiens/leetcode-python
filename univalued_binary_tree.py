# Benjamin Wiens
# Univalued Binary Tree (https://leetcode.com/problems/univalued-binary-tree/)
# BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val
        # deque supports fast poplefts (queue/fifo operations)
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.val or node.val == 0:
                    print(node.val)
                    if value != node.val:
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return True
