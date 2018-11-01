#!/usr/bin/python
import math
#Benjamin Wiens
#https://leetcode.com/problems/binary-search/

unsorted = [21, 4, 1, 5, 19, 3, 25]
unsorted.sort()

def binary_search(target, array):
    l = 0
    r = len(unsorted)
    while l <= r:
        #find the middle element
        m = math.floor((l + r) // 2)
        #print(array[m])
        if array[m] == target:
            return m
        if target > array[m]:
            l = m + 1
        if target < array[m]:
            r = m - 1
    return -1

print(binary_search(25, unsorted))
