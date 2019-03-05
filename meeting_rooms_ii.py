#!/usr/bin/python
#Benjamin Wiens
#Meeting Rooms II (https://leetfree.com/problems/meeting-rooms-ii.html)
#Leetcode Accepted

import heapq
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution:
    def minMeetingRooms(self):
        #if not intervals:
        #    return 0
	#to run locally, set the intervals:
        intervals = [Interval(26, 29), Interval(19, 26), Interval(19, 28), Interval(14, 19), Interval(4,25)]
        heap, count = [], 0
        #sort meetings by their start time
        intervals.sort(key=lambda x: x.start)
        #add first meeting's end time to heap and increase count
        heapq.heappush(heap,intervals[0].end)
        count +=1
        for i in intervals[1:]:
            if i.start < heap[0]:
                #allocate new room and add to heap
                count +=1
                heapq.heappush(heap,i.end)
            #heap top room is free (with min end time)
            elif i.start >= heap[0]:
                #remove the time
                heapq.heappop(heap)
                #add new time
                heapq.heappush(heap,i.end)
        #could also return length of heap
        return count

print(Solution().minMeetingRooms())
