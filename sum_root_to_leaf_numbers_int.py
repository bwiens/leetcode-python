# Benjamin Wiens
# Sum Root to Leaf Numbers (https://leetcode.com/problems/sum-root-to-leaf-numbers/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result, path = [], 0
        def traverse(root, result, path):
            if not root:
                return
            else:
                path = path * 10 + root.val
            if not root.left and not root.right:
                result.append(path)
            if root.left:
                traverse(root.left, result, path)
            if root.right:
                traverse(root.right, result, path)
        traverse(root, result, path)
        ans = 0
        for integer in result:
            ans += integer
        return ans
