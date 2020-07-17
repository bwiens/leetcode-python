# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                stack.extend([node.right, node.left])
        return root
