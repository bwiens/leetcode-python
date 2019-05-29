#!/usr/bin/python
# Benjamin Wiens
# Next Greater Element I (https://leetcode.com/problems/next-greater-element-i/)
# Leetcode Accepted
nums1 = [2,4]
nums2 = [1,2,3,4]

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        #create a hashmap with next greater index
        stack, result = [],[]
        hmap = {}
        for index, number in enumerate(nums2):
            #if empty or current is smaller
            if not stack or number <= stack[-1]:
                stack.append(number)
            else:
                while stack and number > stack[-1]:    
                    hmap[stack.pop()] = number
                stack.append(number)
        #remaining elements that have no greater
        while stack:
            hmap[stack.pop()] = -1
        for number in nums1:
            result.append(hmap.get(number))
        return result

print(Solution().nextGreaterElement(nums1,nums2))
#Runtime O(m+n)
