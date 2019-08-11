#!/usr/bin/python
# Benjamin Wiens
# Add to Array Form of Integer (https://leetcode.com/problems/add-to-array-form-of-integer/)

numbers = [1,2,0,0]
K = 34
class Solution:
    def addToArrayForm(self, A, K):
        string = ''
        result = []
        for number in A:
            string = string + str(number)
        string = str(int(string) + K)
        for char in string:
            result.append(int(char))
        return result

print(Solution().addToArrayForm(numbers, K))
