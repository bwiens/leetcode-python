#!/usr/bin/python
# Benjamin Wiens
# Rotated Digits (https://leetcode.com/problems/rotated-digits)

number = 857
class Solution:
    def rotatedDigits(self, N):
        result = 0
        invalid = False
        for i in range(1, N+1):
            invalid = False
            for j in str(i):
                #these are invalid
                if j in ['3', '4', '7']:
                    invalid = True
                    continue
            if not invalid:        
                for j in str(i):
                    #these make it valid
                    if j in ['6', '9', '2', '5']:
                        result += 1
                        break
        return result

print(Solution().rotatedDigits(number))
