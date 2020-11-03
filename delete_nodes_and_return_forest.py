from collections import deque
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if not root:
            return
        result = []
        queue = deque([(root, False)])
        while queue:
            node, has_parent = queue.popleft()
            if not has_parent and node.val not in to_delete:
                result.append(node)
            if node.val in to_delete:
                has_parent = False
            else:
                has_parent = True
            if node.left:
                queue.append((node.left, has_parent))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                queue.append((node.right, has_parent))
                if node.right.val in to_delete:
                    node.right = None
        return result
                    
