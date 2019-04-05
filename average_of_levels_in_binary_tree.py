# Benjamin Wiens
# Average of Levels in Binary Tree (https://leetcode.com/problems/average-of-levels-in-binary-tree)
# Leetcode Accepted

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        #need to use deque for first node (root)
        queue = deque([root])
        if not root: return []
        result, tmp = [], []
        while queue:
            #need to use range
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)
            result.append(sum(tmp)/len(tmp))
            tmp = []
        return(result)
