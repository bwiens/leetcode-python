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
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            if val < node.val:
                if node.left:
                    stack.append(node.left)
            else:
                if node.right:
                    stack.append(node.right)
        return None
