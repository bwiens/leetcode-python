# Benjamin Wiens
# Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        output = [root.val]
        tmp = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                output.append(queue[-1].val)
        return output
