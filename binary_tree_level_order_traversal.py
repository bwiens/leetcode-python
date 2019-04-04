# Benjamin Wiens
# Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal)
# Leetcode Accepted

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque([root,])
        result, tempresult = [], []
        if not root: return []
        # iterate through the tree, queuing each node, their left and right child. at each level, add val to result
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                tempresult.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:      
                    queue.append(node.right)
            result.append(tempresult)
            tempresult = []
        return result

# Runtime: O(n) for both space and time
