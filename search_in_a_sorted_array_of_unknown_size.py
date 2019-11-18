# Benjamin Wiens
# Search in a Sorted Array of Unknown Size (https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/)

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        #find right boundary
        left = 0
        right = 1
        while target > reader.get(right):
            left = right
            right = right * 2
            # we could shift to be faster right <<= 1
        # now binary search within the boundaries
        while left <= right:
            # don't forget the brackets
            m = (right + left) // 2
            # no overflow protection needed because python has arbitrary precision (integer is only limited by memory available)
            if reader.get(m) == target:
                return m
            elif reader.get(m) < target:
                left = m + 1
            else:
                right = m -1
        return -1
                
