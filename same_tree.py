#!/usr/bin/python
# Benjamin Wiens
# Same Tree (https://leetcode.com/problems/same-tree)
# Leetcode Accepted

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if both nodes are empty:
        if not p and not q:
            return True
        #if only one exists
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
