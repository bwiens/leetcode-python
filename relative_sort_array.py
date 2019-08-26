#!/usr/bin/python
# Benjamin Wiens
# Relative Sort Array (https://leetcode.com/problems/relative-sort-array/)

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()
        count, arr2_hmap, result = {}, {}, []
        for number in arr2:
            arr2_hmap[number] = None
        for number in arr1:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        for number in arr2:
            x = count.get(number)
            for i in range(x):
                result.append(number)
        for number in arr1:
            if number not in arr2_hmap:
                result.append(number)
        return result

print(Solution().relativeSortArray(arr1,arr2))
