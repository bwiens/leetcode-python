#!/usr/bin/python
# Benjamin Wiens
# Maximize Distance to Closest Person (https://leetcode.com/problems/maximize-distance-to-closest-person)
# Leetcode Accepted

seats = [1, 0, 0, 0, 0]

import math
class Solution:
    def maxDistToClosest(self, seats):
        maximum, emptycount = 0,0
        found1 = False
        for index, seat in enumerate(seats):
	    # emptycount is the number of 0s
            if seat == 0:
                emptycount += 1
            if seat == 1:
                if emptycount != 0:
                    if found1 == True:
	                # if we had a 1 before, we must sit at half the distance
                        if maximum < math.ceil(emptycount / 2):
                            maximum = math.ceil(emptycount / 2)
                    else:
                        if maximum < emptycount:
                            maximum = emptycount
                emptycount = 0
                found1 = True
            # if the emptycount is not zero and we're at the end, we can sit on the edge
            if index == len(seats)-1:
                if maximum < emptycount:
                    maximum = emptycount
        return maximum
print(Solution().maxDistToClosest(seats))
