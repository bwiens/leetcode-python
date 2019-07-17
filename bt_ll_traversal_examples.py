#Binary Tree traversal with Queue (Breadth-first search / In Order)
from collections import deque
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:       
        queue = deque([root])
        sumz = 0
        while queue:
            node = queue.popleft()
            if node.val <= R and node.val >= L:
                sumz += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sumz

#Binary Tree traversal through recursion (Depth-first search)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:       
        def traverseBST(root,L,R):
            if not root:
                return
            if root.val >= L and root.val <= R:
                self.sumz += root.val
            traverseBST(root.left,L,R)
            traverseBST(root.right,L,R)
        self.sumz = 0
        traverseBST(root,L,R)
        return self.sumz

#Linked List traversal (iteratively)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        result = []
        while head:
            result.append(head)
            head = head.next
        return result[(len(result)//2)]

#Linked List traversal (recursively)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        self.result = []
        def traverse(head):
            if not head:
                return
            self.result.append(head)
            traverse(head.next)
        traverse(head)
        return self.result[(len(self.result)//2)]
# remember to use self. if it needs to be global 
