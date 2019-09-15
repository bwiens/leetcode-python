#!/usr/bin/python
# Benjamin Wiens
# Maximum Number of Balloons (https://leetcode.com/problems/maximum-number-of-balloons/)

balloons = "loonbalxballpoon"

class Solution:
    def maxNumberOfBalloons(self, text):
        hmap, count = {}, 0
        for index, char in enumerate(text):
            if char in hmap:
                hmap[char] += 1
            else:
                hmap[char] = 1
        changed = True
        while changed:
            for char in 'balloon':
                if char not in hmap:
                    return count
                else:
                    if hmap.get(char) == 1:
                        del hmap[char]
                    else:
                        hmap[char] -= 1
            count += 1
        return count
            
print(Solution().maxNumberOfBalloons(balloons))
