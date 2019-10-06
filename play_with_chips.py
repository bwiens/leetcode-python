#!/usr/bin/python
# Benjamin Wiens
# Play With Chips (https://leetcode.com/problems/play-with-chips/)

chips = [2,2,2,3,3]

class Solution:
    def minCostToMoveChips(self, chips):
        #The key observation here is that it's free to move a chip from an even number to another even number, and it is free to move a chip from an odd number to another odd number
        #count even and odd chips
        even, odd = 0, 0
        for chip in chips:
            if chip % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even,odd)

print(Solution().minCostToMoveChips(chips))
