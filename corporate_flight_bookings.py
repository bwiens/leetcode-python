#!/usr/bin/python
# Benjamin Wiens
# Corporate Flight Bookings (https://leetcode.com/problems/corporate-flight-bookings)

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
class Solution:
    def corpFlightBookings(self, bookings, n):
        result = [0] * (n+1)
        #mark the deltas (head and tail)
        for booking in bookings:
            #start
            result[booking[0]-1] += booking[2]
            #end
            result[booking[1]] -= booking[2]
        #cumulative sum processing
        tmp = 0
        for i in range(n):
            tmp += result[i]
            result[i] = tmp
        return result[:n]

print(Solution().corpFlightBookings(bookings,n))
