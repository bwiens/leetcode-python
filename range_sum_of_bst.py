# Benjamin Wiens
# Range Sum of BST
# Leetcode Accepted (https://leetcode.com/problems/range-sum-of-bst/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sums = 0 
        def dfs(node):
            if node:
                #if between range
                if node.val >= L and node.val <= R:
                    self.sums += node.val
                #explore right if val smaller than R
                if node.val < R:
                    dfs(node.right)
                #explore left if val larger than L
                if node.val > L:
                    dfs(node.left)
        dfs(root)
        return self.sums                

# O(n)                    
