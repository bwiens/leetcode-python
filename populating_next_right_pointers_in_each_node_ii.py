# Benjamin Wiens
# Populating Next Right Pointers in Each Node II (https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

"""
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = deque([root])
        while queue:
            # don't forget to set the length here, as it will change
            length = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i <= length -2:
                    node.next = queue[0]
                #print(node.val, node.next)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
