class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # the + 1 here is the key
            height = max(left, right) + 1
            if height > len(result):
                result.append([])
            result[height-1].append(root.val)
            return height
        result = []
        dfs(root)
        return result
