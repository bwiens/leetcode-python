# Benjamin Wiens
# Linked List Cycle (https://leetcode.com/problems/linked-list-cycle/)
# Leetcode Accepted

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hset = set()
        while head:
            if head in hset:
                return True
            else:
                hset.add(head)
            head = head.next
        return False

constant space:

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while slow and fast:
            if slow == fast:
                return slow
            else:
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    return None
        return None
            
