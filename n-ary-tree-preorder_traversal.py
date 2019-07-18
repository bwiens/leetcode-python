# Benjamin Wiens
# N-ary Tree Preorder Traversal (https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            #reverse the children to remain stack order for dfs
            stack.extend(node.children[::-1])
        return result
