#!/usr/bin/python
# Benjamin Wiens
# Path Sum II (https://leetcode.com/problems/path-sum-ii/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path, result = [], []
        def traverse(root, sum, path):
            if not root:
                return
            #the sum == root.val stems from having to subtract the last value
            if not root.left and not root.right and sum == root.val:
                result.append(path + [root.val])
                #print(result)
            if root.left:
                traverse(root.left, sum - root.val, path + [root.val])
            if root.right:
                traverse(root.right, sum - root.val, path + [root.val])
        traverse(root,sum, path)
        return result
        
            
            
