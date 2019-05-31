#!/usr/bin/python
# Benjamin Wiens
# Intersection of Two Arrays (https://leetcode.com/problems/intersection-of-two-arrays-ii/)
# Leetcode Accepted

array1 = [1,2,2,1]
array2 = [2,2]
class Solution:
    def intersect(self, nums1, nums2):
        hmap1, hmap2 = {}, {}
        result = []
        for number in nums1:
            if number in hmap1:
                hmap1[number] += 1
            else:
                hmap1[number] = 1
        for number in nums2:
            if number in hmap2:
                hmap2[number] += 1
            else:
                hmap2[number] = 1
        for key, value in hmap1.items():
            if key in hmap2:
                for i in range(min(value, hmap2.get(key))):
                    result.append(key)
        return result

print(Solution().intersect(array1,array2))
