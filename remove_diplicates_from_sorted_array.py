#!/usr/bin/python
#Benjamin Wiens
#Remove Duplicates From Sorted Array (https://leetcode.com/problems/remove-duplicates-from-sorted-array)
#Leetcode Accepted

input = [0,0,1,1,1,2,2,3,3,4]


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        c = 0
        #keep c the same if nums[c] is same as i
        for i in nums:
            #when it discover a new numer, advance c and overwrite the duplicate
            if i != nums[c]:
                c += 1
                nums[c] = i
            print(nums)
        return c + 1

print(Solution().removeDuplicates(input))
