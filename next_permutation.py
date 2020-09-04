#!/usr/bin/python

input = [1,2,3]
class Solution:
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        # find the first descending number (from right) #right-> left
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
         # nums are in descending order
        if i == 0:  
            nums.reverse()
            return 
        # find tthe one "just bigger"
        k = i - 1    
        while nums[j] <= nums[k]:
            j -= 1
        # swap
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  
        # reverse the tail
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
        return nums

print(Solution().nextPermutation(input))
