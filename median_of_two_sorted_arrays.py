#!/usr/bin/python
#Benjamin Wiens
#Median of Two Sorted Arrays (https://leetcode.com/problems/median-of-two-sorted-arrays/)
#Leetcode Accepted
import math
nums1 = [1, 3]
nums2 = [3, 4]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type: nums1: List[int]
        :type: nums2: List[int]
        :return: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        #even
        length = (len(nums1)) -1
        if len(nums1) % 2 == 0:
            x = (nums1[math.floor(length // 2)] + nums1[math.floor(length // 2) + 1]) / 2
        #odd
        else:
            x = nums1[(length//2)]
        return x

print(Solution().findMedianSortedArrays(nums1, nums2))
