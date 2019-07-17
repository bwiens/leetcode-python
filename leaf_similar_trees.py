# Benjamin Wiens
# Leaf-Similiar Trees (https://leetcode.com/problems/leaf-similar-trees/)

class Solution:
    def leafSimilar(self, root1, root2):
        def trim(root):
            if not root:
                return
            else:
                if not root.right and not root.left:
                    result.append(root.val)
                trim(root.left)
                trim(root.right)
        result, result2 = [],[]
        trim(root1)
        result2 = result.copy()
        result = []
        trim(root2)
        if result == result2:
            return True
        else:
            return False
