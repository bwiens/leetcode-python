#!/usr/bin/python
#Benjamin Wiens
#Intersection of Two Arrays (https://leetcode.com/problems/intersection-of-two-arrays/)
#Leetcode Accepted

a1 = [1,2,2,1] 
a2 = [2,2]

class Solution:
    def intersection(self, nums1, nums2):
        result, numsdict = [], {}
        for i in nums1:
            if i not in numsdict:
                numsdict[i] = None
        for i in set(nums2):
            if i in numsdict:
                result.append(i)
        return(result)

print(Solution().intersection(a1,a2))
