# Benjamin Wiens
# Two Sum BSTs (https://leetcode.com/problems/two-sum-bsts/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        result1, result2 = {}, {}
        def traverse(root, array):
            if not root:
                return
            array[root.val] = 1
            if root.left:
                traverse(root.left, array)
            if root.right:
                traverse(root.right, array)
        traverse(root1, result1)
        traverse(root2, result2)
        for num1 in result1:
            compliment = target-num1
            if compliment in result2:
                    return True
        return False
