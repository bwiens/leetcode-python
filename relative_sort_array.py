#!/usr/bin/python
# Benjamin Wiens
# Relative Sort Array (https://leetcode.com/problems/relative-sort-array/)

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1, arr2):
        counted = Counter(arr1)
        arr2set = set(arr2)
        result, tail = [], []
        for number in arr2:
            for i in range(counted[number]):
                result.append(number)
        for number in arr1:
            if number not in arr2set:
                tail.append(number)
        tail.sort()
        for number in tail:
            result.append(number)
        return result

print(Solution().relativeSortArray(arr1,arr2))
