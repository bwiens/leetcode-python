#!/usr/bin/python
# Benjamin Wiens
# How Many Apples Can You Put Into the Basket (https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/)

arr = arr = [100,200,150,1000]

class Solution:
    def maxNumberOfApples(self, arr):
        arr.sort()
        summation, cnt = 0, 0
        for number in arr:
            if summation + number < 5000:
                summation += number
                cnt += 1
            else:
                break
        return cnt

print(Solution().maxNumberOfApples(arr))
