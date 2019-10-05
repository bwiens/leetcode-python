#!/usr/bin/python
# Benjamin Wiens
# Intersection of Three Sorted Arrays (https://leetcode.com/problems/intersection-of-three-sorted-arrays/)

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

from collections import OrderedDict
class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        hmap = OrderedDict()
        result = []
        for num1 in arr1:
            if num1 not in hmap:
                hmap[num1] = 1
        for num2 in arr2:
            if num2 not in hmap:
                hmap[num2] = 1
            else:
                hmap[num2] += 1
        for num3 in arr3:
            if num3 not in hmap:
                hmap[num3] = 1
            else:
                hmap[num3] += 1
        for key, value in hmap.items():
            if value == 3:
                result.append(key)
        return result

print(Solution().arraysIntersection(arr1,arr2,arr3))
