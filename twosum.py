#!/usr/bin/python
#Benjamin Wiens
#Two Sum Problem
#Leetcode Accepted
   
nums = [2, 7, 11, 15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numdict, x = {}, 0
        #create hashtable
        for index, i in enumerate(nums):
            numdict[i] = index
        for index, i in enumerate(nums):
            x = target - i
            if x in numdict:
                if index != numdict.get(x):
                    return index, numdict.get(x)
print(Solution().twoSum(nums, target))

#Time Complexity: O(n). We traverse the list containing n elements exactly twice. 
#Since the hash table reduces the look up time to O(1), the time complexity is O(n)
#Space Complexity:  O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly nn elements.
