#!/usr/bin/python
# Benjamin Wiens
# Student Attendance Record I (https://leetcode.com/problems/student-attendance-record-i)
# Leetcode Accepted

record = "PPALLP"

class Solution:
    def checkRecord(self, s):
        #BALLL
        #01234
        #length = 5
        first_a = False
        length = len(s)
        for index, char in enumerate(s):
            if char == 'L':
                if index <= length - 3:
                    if s[index+1] == 'L':
                        if s[index+2] == 'L':
                            return False
            if char == 'A':
                if first_a:
                    return False
                else:
                    first_a = True
        return True

print(Solution().checkRecord(record))
