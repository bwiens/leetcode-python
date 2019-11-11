# Benjamin Wiens
# Binary Tree Paths (https://leetcode.com/problems/binary-tree-paths/)

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result, string = [], ''
        def traverse(root, string, result):
            if not root:
                return
            if not root.left and not root.right:
                string = string + '->' + str(root.val)
                result.append(string[2:])
                return result
            if root.left:
                traverse(root.left, string + '->' + str(root.val), result)
            if root.right:
                traverse(root.right, string + '->' + str(root.val), result)
        traverse(root,string,result)
        return result
