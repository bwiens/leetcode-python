# Benjamin Wiens
# Subtree of Another Tree (https://leetcode.com/problems/subtree-of-another-tree/)

# Warning: Very verbose, needs to be improved
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        result1, result2 = [], []
        def traverse(root, array):
            if not root:
                return
            array.append(root.val)
            if root.left:
                traverse(root.left, array)
            else:
                array.append('lnull')
                traverse(root.left, array)
            if root.right:
                traverse(root.right, array)
            else:
                array.append('lright')
                traverse(root.left, array)
                
        traverse(s, result1)
        traverse(t, result2)
        print(result1, result2)
        i = 1
        for index, el in enumerate(result1):
            print(el)
            if el == result2[0]:
                if len(result2) == 3:
                    if index == len(result1) -1 or (result1[index+1] == 'lnull' and result1[index+2] == 'rnull'): 
                                                    return True
                while result1[index+i] == result2[i]: 
                    i += 1
                    if i == len(result2):
                        return True    
        return False
