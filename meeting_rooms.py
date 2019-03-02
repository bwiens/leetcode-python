#Benjamin Wiens
#Meeting Rooms (https://leetcode.com/problems/meeting-rooms/submissions/)
#Leetcode Accepted

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
		#sort by start time
        intervals.sort(key=lambda x:x.start)
        helper = []
        for index, i in enumerate(intervals):
            #get the first element
            if not helper:
                helper.append(i)
            else: 
				#for each interval, see if the prior has a later end time than current start time
                if helper[index-1].end > i.start:
                      return False
                else:
                    helper.append(i)
        return True
