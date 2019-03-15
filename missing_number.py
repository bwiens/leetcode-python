#!/usr/bin/python
#Benjamin Wiens
#Missing Number (https://leetcode.com/problems/missing-number/)
#Leetcode Accepted
input = [3,0,1]
class Solution:
    def missingNumber(self, nums):
        #slow version: (nlogn)
 #        nums.sort()
 #       for i, el in enumerate(nums):
 #           if i != el:
 #               return i
 #       return nums[-1]+1
    
        #fast version O(n)
        #in case there are duplicates
        nums_set = set(nums)
        #create hashtable
        ndict = {}
        for el in nums_set:
            ndict[el] = None
        #one number will always be missing
        total = len(nums_set) + 1
        for i in range(total):
            if i not in ndict:
                return i

print(Solution().missingNumber(input))
