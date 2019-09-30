#!/usr/bin/python
#Benjamin Wiens
#Meeting Rooms II (https://leetfree.com/problems/meeting-rooms-ii.html)

meetings = [[0, 30],[5, 10],[15, 20]]

import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort()
        count = 1
        #add first end to heap
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] < rooms[0]:
                # need a new room
                count += 1
                heapq.heappush(rooms, interval[1])
            else:
                # the top room is free
                heapq.heappop(rooms)
                # add the new end time to the heap
                heapq.heappush(rooms, interval[1])
        return count

print(Solution().minMeetingRooms(meetings))
