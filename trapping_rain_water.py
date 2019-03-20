#!/usr/bin/python
# Benjamin Wiens
# Trapping Rain Water (https://leetcode.com/problems/trapping-rain-water/)
# Leetcode Accepted

height = [0,1,0,2,1,0,1,3,2,1,2,1]

class Solution:
    def trap(self, height):
        #the given list is an elevation map
        lmax, rmax, water = 0, 0, 0
        left, right = 0, len(height) - 1
        while left < right:
            #water is dictated by the lowest minimum surrounding
            if height[left] < height[right]: #the < is the key (lowest) min surrounding
                if height[left] >= lmax:
                    lmax = height[left]
                water += lmax - height[left]
                #print("left", lmax, height[left], water)
                left += 1
            else:
                if height[right] >= rmax:
                    rmax = height[right]
                water += rmax - height[right]
                right -= 1
                #print("right", rmax, height[right], water)
        return water

print(Solution().trap(height))
