#!/usr/bin/python

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8

class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if start + duration <= end:
                return [start, start+duration]
            # this didn't work out
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []

print(Solution().minAvailableDuration(slots1, slots2, duration))
