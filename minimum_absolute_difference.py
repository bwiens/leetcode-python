#!/usr/bin/python
# Benjamin Wiens
# Minimum Absolute Difference (https://leetcode.com/problems/minimum-absolute-difference/)

arr = [3,8,-10,23,19,-4,-14,27]

class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        minimum, result = arr[1]-arr[0], []
        for index, number in enumerate(arr[1:], 1):
            current_min = number-arr[index-1]
            if current_min < minimum:
                minimum, result = current_min, []
                result.append([arr[index-1], number])
            elif current_min == minimum:
                result.append([arr[index-1], number])
        return result

print(Solution().minimumAbsDifference(arr))
