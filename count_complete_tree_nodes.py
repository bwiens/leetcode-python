# Benjamin Wiens
# Count Complete Tree Nodes (https://leetcode.com/problems/count-complete-tree-nodes)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        left = root
        right = root
        countl, countr = 0, 0
        # check how many left
        while left:
            countl += 1
            left = left.left
        while right:
            countr += 1
            right = right.right
        # check if it's a perfect binary tree 2h + 1 – 1 
        if countl == countr:
            return (2**countr) -1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
