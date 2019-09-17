#!/usr/bin/python
# Benjamin Wiens
# Maximum Number of Balloons (https://leetcode.com/problems/maximum-number-of-balloons/)

balloons = "loonbalxballpoon"

import sys
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        minimum = sys.maxsize 
        letters = ['b','a','l','o','n']
        for letter in letters:
            if letter == 'l' or letter == 'o':
                minimum = min(minimum, text.count(letter)//2)
            else:
                minimum = min(minimum, text.count(letter))
        return minimum
            
print(Solution().maxNumberOfBalloons(balloons))
