#!/usr/bin/python
# Benjamin Wiens
# Armstrong Number (https://leetcode.com/problems/armstrong-number/)

number = 153

class Solution:
    def isArmstrong(self, N):
        strnr = str(N)
        rolling_sum = 0
        length = len(strnr)
        for char in strnr:
            rolling_sum += int(char)**length
        if rolling_sum == N:
            return True
        else:
            return False

print(Solution().isArmstrong(number))
