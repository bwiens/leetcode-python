# Benjamin Wiens
# Maximum Binary Tree (https://leetcode.com/problems/maximum-binary-tree/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        root = TreeNode(max(nums))
        left, right = self.break_array(root.val, nums)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root
    
    # break array into left and right subtrees 
    def break_array(self, root,nums):
        if not nums:
            return ([],[])
        index = nums.index(root)
        return (nums[:index], nums[index+1:])
