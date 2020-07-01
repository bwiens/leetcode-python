#!/usr/bin/python
# Benjamin Wiens
# Next Greater Element I (https://leetcode.com/problems/next-greater-element-i/)
# Leetcode Accepted
nums1 = [2,4]
nums2 = [1,2,3,4]

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dict = {}
        stack, result = [],[]
        for index, number in enumerate(nums2):
            while stack and stack[-1] < number:
                dict[stack.pop()] = number
            stack.append(number)
        for number in nums1:
            if number in dict:
                result.append(dict.get(number))
            else:
                result.append(-1)
        return result

print(Solution().nextGreaterElement(nums1,nums2))
#Runtime O(m+n)
