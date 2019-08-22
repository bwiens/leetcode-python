# Benjamin Wiens
# Minimum Absolute Difference in BST (https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
# This is not optimal (yet) as we only have to compare adjacent elements because of the BST properties. Will do this later.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
import sys
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        dif = sys.maxsize
        result.sort()
        for index, number in enumerate(result[:len(result)-1]):
            dif = min(dif, abs(number - result[index+1]))
        return dif
