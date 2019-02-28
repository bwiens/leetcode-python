#Benjamin Wiens
#First Bad Version (https://leetcode.com/problems/first-bad-version/)
#The isBadVersion function is provided by leetcode
#Leetcode Accepted
import sys
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            #found one bad call
            if isBadVersion(mid):
                #found the first bad call
                if not isBadVersion(mid-1):
                    return mid
                #check left side
                else:
                    right = mid - 1
            #check right side
            else:
                left = mid + 1
