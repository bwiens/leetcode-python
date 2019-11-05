#!/usr/bin/python
# Benjamin Wiens
# Linked List
# Leetcode Accepted (https://leetcode.com/problems/middle-of-the-linked-list/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        result = []
        while head:
            result.append(head)
            head = head.next
        if len(result) < 3: 
            return result[-1]
        else:
            return result[(len(result)//2)]

#O(1) Space:

    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        dummy = head
        while head:
            count += 1
            head = head.next
        count = (count // 2) + 1 # or math.ceil()
        if count == 0:
            return dummy.next
        i = 1
        print(count)
        while dummy:
            if count == i:
                return dummy
            i += 1
            dummy = dummy.next
