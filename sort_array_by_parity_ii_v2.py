#!/usr/bin/python
# Benjamin Wiens
# Sort Array by Parity II (https://leetcode.com/problems/sort-array-by-parity-ii/) One Pass

numbers = [4,2,5,7]

class Solution:
    def sortArrayByParityII(self, A):
        result = [0] * len(A)
        odd, even = 1, 0
        for number in A:
            if number % 2 == 0:
                result[even] = number
                even += 2
            else:
                result[odd] = number
                odd += 2
        return result

print(Solution().sortArrayByParityII(numbers))
