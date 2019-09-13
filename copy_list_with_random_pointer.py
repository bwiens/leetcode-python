# Benjamin Wiens
# Copy List With Random Pointer (https://leetcode.com/problems/copy-list-with-random-pointer/)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hmap = {None: None}
        node = head
	# create copies of nodes. remember we only know what the current val is
        while node:
            hmap[node] = Node(node.val, None, None)
            node = node.next
        node = head
        # after this we can actually lookup the next pointer (prev we are only before the next) because all nodes are in there
        while node:
            #mp[p] gets the copy of p
            #right hand side gets the copy of the next node
            hmap[node].next = hmap[node.next]
            hmap[node].random = hmap[node.random]
            node = node.next
        # return the copy
        return hmap[head]
