# Benjamin Wiens
# Binary Tree Level Order Traversal II
# Leetcode Accepted (https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = deque([root])
        result, tmp = deque(), []
        #use a queue to pop as we traverse
        while queue:
            #process the queue at each level
            for i in range(len(queue)):
                #popleft (queue)
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)
            #queue (appendleft)
            result.appendleft(tmp)
            tmp = []
        return result
