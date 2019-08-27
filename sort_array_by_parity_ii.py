#!/usr/bin/python
# Benjamin Wiens
# Sort Array by Parity II (https://leetcode.com/problems/sort-array-by-parity-ii/)

numbers = [4,2,5,7]

class Solution:
    def sortArrayByParityII(self, A):
        even, odd, result = [], [], []
        for number in A:
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
        for i in range(len(A)):
            if i % 2 == 0:
                result.append(even.pop())
            else:
                result.append(odd.pop())
        return result

print(Solution().sortArrayByParityII(numbers))
