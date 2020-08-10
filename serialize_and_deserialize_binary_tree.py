# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return
        serialize = []
        queue = deque([root])
        while queue:
            #use deque for fast popleft()
            node = queue.popleft()
            if node:
                # key here, sicne we need to account for null values at right point
                queue.append(node.left)
                queue.append(node.right)
                serialize.append(node.val)
            else:
                serialize.append('#')
        while serialize[-1] == '#':
            serialize.pop() # Strip trailing '#' nodes.
        return serialize

    def deserialize(self, data):
        if not data: return []
        root = TreeNode(data[0])
        queue = deque([root])
        i = 1
        while queue and i < len(data):
            node = queue.popleft()
            if data[i] != '#':
                left = TreeNode(data[i])
                node.left = left
                queue.append(left)
            i += 1
            if i >= len(data):
                break
            if data[i] != '#':
                right = TreeNode(data[i])
                node.right = right
                queue.append(right)
            i += 1
        return root
            
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
