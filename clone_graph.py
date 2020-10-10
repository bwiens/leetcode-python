"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        queue = deque([node])
        # add this here and you won't need to check after queue.popleft()
        # create Node as value
        map = {node: Node(node.val)}
        while queue:
            nd = queue.popleft()
            for neighbor in nd.neighbors:
                if neighbor not in map:
                    queue.append(neighbor)
                    # create Node as value
                    map[neighbor] = Node(neighbor.val)
                map[nd].neighbors.append(map[neighbor])
        return map[node]
