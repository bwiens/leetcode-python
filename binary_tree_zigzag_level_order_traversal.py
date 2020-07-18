# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result = []
        right_direction = False
        queue = collections.deque([root])
        while queue:
            tmp = collections.deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if right_direction:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp)
            right_direction = not right_direction
        return result
        
