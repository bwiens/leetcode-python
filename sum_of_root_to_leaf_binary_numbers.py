#!/usr/bin/python
# Benjamin Wiens
# Sum of Root to Leaf Binary Numbers (https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        binstr = ''
        sum_ = 0
        def traverse(root, binstr):
            # reached a leaf
            if not root:
                return
            if not root.left and not root.right:
                result.append(binstr + str(root.val))
            if root.left:
                traverse(root.left, binstr + str(root.val))
            if root.right:
                traverse(root.right, binstr + str(root.val))
        traverse(root, binstr)
        for binary in result:
            sum_ += int(binary, 2)
        return sum_
