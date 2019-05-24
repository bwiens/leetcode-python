# Benjamin Wiens
# Path Sum (https://leetcode.com/problems/path-sum)
# Leetcode Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        #leaf node
        if not root.left and not root.right:
            if sum == 0:
                return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)  
