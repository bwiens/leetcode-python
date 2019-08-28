# Benjamin Wiens
# Binary Search Tree to Greater Sum Tree (https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum_ = 0
        def traverse(node):
            if not node:
                return
	    # travese right subtree to get greater sum
            if node.right:
                traverse(node.right)
            self.sum_ += node.val
	    # assign greater sum value
            node.val = self.sum_
            if node.left:
                traverse(node.left)
        traverse(root)
        return root
