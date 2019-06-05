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
        hmap = {}
        if not head or not head.next:
            return False
        while head:
            if head in hmap:
                return True
            else:
                hmap[head] = None
            head = head.next
            print(hmap)
        return False
