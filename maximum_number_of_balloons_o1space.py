#!/usr/bin/python
# Benjamin Wiens
# Maximum Number of Balloons (https://leetcode.com/problems/maximum-number-of-balloons/)

balloons = "loonbalxballpoon"

import sys
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        minimum = sys.maxsize 
        hmap = {1: 'b', 2: 'a', 3: 'l', 4: 'o', 5: 'n'}
        for key, value in hmap.items():
            if value == 'l' or value == 'o':
                minimum = min(minimum, text.count(value)//2)
            else:
                minimum = min(minimum, text.count(value))
        return minimum
            
print(Solution().maxNumberOfBalloons(balloons))
