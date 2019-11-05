# Benjamin Wiens
# Remove nth Node From End of List (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
# Two Pass Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 1 and not head.next:
            return 
        count = 0
        dummy = current = head
        # count number of nodes
        while head:
            count += 1
            head = head.next
        remove = count - n
        # if head needs to be cut
        if remove == 0:
            return current.next
        while current:
            remove -= 1
            if remove == 0:
                current.next = current.next.next
                return dummy
            current = current.next
        return dummy
