# Benjamin Wiens
# Closest Binary Search Tree Value (https://leetcode.com/problems/closest-binary-search-tree-value/)

from sys import maxsize
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:    
        self.minimum = sys.maxsize
        self.result = root.val
        def traverse(root):
            if not root:
                return
            if self.minimum > abs(root.val-target):
                self.result = root.val
                self.minimum = abs(root.val-target)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(root)
        return self.result
