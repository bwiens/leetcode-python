# Benjamin Wiens
# Minimum Depth of Binary Tree (https://leetcode.com/problems/minimum-depth-of-binary-tree/) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = []
        path = 1
        def traverse(root, path):
            if not root:
                return
            # reached a lef
            if not root.left and not root.right:
                depth.append(path)
            if root.left:
                traverse(root.left, path+1)
            if root.right:
                traverse(root.right, path+1)
        traverse(root, path)
        return min(depth)
