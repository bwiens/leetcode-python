# Benjamin Wiens
# Search in a Binary Search Tree BFS (https://leetcode.com/problems/search-in-a-binary-search-tree/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.val == val:
                    return node
                if val < node.val:
                    if node.left:
                        queue.append(node.left)
                else:
                    if node.right:
                        queue.append(node.right)
