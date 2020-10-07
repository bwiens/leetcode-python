import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q, result = [], []
        for list in lists:
            while list:
                heapq.heappush(q, list.val)
                list = list.next
        dummy = n = ListNode(0)
        while q:
            node = ListNode(heapq.heappop(q))
            n.next = node
            n = n.next
        return dummy.next
