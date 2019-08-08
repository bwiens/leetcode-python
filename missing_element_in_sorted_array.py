#!/usr/bin/python
# Benjamin Wiens
# Missing Element (https://leetcode.com/problems/missing-element-in-sorted-array/)

A = [4,7,9,10]
K = 1

class Solution:
    def missingElement(self, nums, k) -> int:
        result = []
        missing = 0
        for index, number in enumerate(nums[1:], 1) :
            if number - nums[index-1] > 1:
                #add the difference to get missing numbers
                missing += number - nums[index-1] - 1
                if k <= missing:
                    if k == missing:
                        return number -1
                    else:
                        #missing is larger than k
                        return number - (missing - k +1)
                    
        #k is larger than missing | k = 10 missing = 3
        missing = k - missing
        return nums[-1] + missing

print(Solution().missingElement(A,K))
#O(n), O(Logn) is possible with binary search
