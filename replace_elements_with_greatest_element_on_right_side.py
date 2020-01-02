#!/usr/bin/python
# Benjamin Wiens
# Replace Elements with Greatest Element on Right Side (https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)

numbers = [17,18,5,4,6,1]
class Solution:
    def replaceElements(self, arr):
        result = [0] * len(arr)
        right = len(arr) - 2
        maximum = arr[-1]
        while right >= 0:
            result[right] = maximum
            maximum = max(arr[right], maximum)
            right -= 1
        result[-1] = -1
        return result

print(Solution().replaceElements(numbers))
