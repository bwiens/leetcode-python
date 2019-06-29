#!/usr/bin/python
# Benjamin Wiens
# Nim Game (https://leetcode.com/problems/nim-game/)
# Leetcode Accepted 

input = 4

class Solution:
    def canWinNim(self, n: int) -> bool:
        #if I take 1, opponent will take 3
        #if I take 2, oponnent will take 2
        #if I take 3, oponnent will take 1
        #thus, anything divisible by 4 and I lose
        if n % 4 == 0:
            return False
        return True

print(Solution().canWinNim(input))

#Time And space is O(1)
