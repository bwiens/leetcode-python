#!/usr/bin/python
# Benjamin Wiens
# Self Dividing Numbers (https://leetcode.com/problems/self-dividing-numbers/)

left = 1, right = 22

class Solution:
    def selfDividingNumbers(self, left,right):
        result = []
        self_div = True
        for i in range(left,right+1):
            for char in str(i):
                if char == '0':
                    self_div = False
                    break
                elif i % int(char) == 0:                
                    continue
                else:
                    self_div = False
                    break
            if self_div:
                result.append(i)
            self_div = True
        return result

print(Solution().selfDividingNumbers(left,right))
