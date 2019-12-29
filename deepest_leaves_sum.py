# Benjamin Wiens
# Deepest Leaves Sum (https://leetcode.com/problems/deepest-leaves-sum/)

from collections import deque
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        sum = 0
        queue = deque([root])
        while queue:
            sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum

