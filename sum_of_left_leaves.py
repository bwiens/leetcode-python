# Benjamin Wiens
# Sum of Left Leaves (https://leetcode.com/problems/sum-of-left-leaves)
# Leetcode Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left:
            #got a left leaf node
            if not root.left.left  and not root.left.right:
                    return root.left.val + self.sumOfLeftLeaves(root.right)
        #is not a leafe
        return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
