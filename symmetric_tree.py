# Benjamin Wiens
# Symmetric Tree (https://leetcode.com/problems/symmetric-tree/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traverse(root1, root2):
            if not root1 and root2:
                return False
            if not root2 and root1:
                return False
            if not root1 and not root2:
                return True
            return root1.val == root2.val and traverse(root1.right, root2.left) and traverse(root1.left, root2.right)
        return traverse(root, root)    
