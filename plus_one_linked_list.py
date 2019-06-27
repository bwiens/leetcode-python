# Benjamin Wiens
# Plus One Linked List (https://leetcode.com/problems/plus-one-linked-list/)
# Leetcode Accepted

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        result = []
        summarize = ''
        while head:
            #print(head.val)
            summarize = summarize + str(head.val)
            head = head.next
        #plus one
        summarize = str(int(summarize) + 1)
        for i in str(summarize):
            result.append(int(i))
        return result

#O(n)
