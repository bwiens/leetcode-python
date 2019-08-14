# Benjamin Wiens
# Search in a Binary Search Tree (https://leetcode.com/problems/search-in-a-binary-search-tree/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root
        if val < root.val:
            if root.left:
                return self.searchBST(root.left, val)
        else:
            if root.right:
                return self.searchBST(root.right, val)
