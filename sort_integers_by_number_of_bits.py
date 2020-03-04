#!/usr/bin/python
# Benjamin Wiens
# Sort Integers by the Number of 1 bits (https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits)

input = [0,1,2,3,4,5,6,7,8]

class Solution:
    def sortByBits(self, arr):
        dict = {}
        result = []
        for number in arr:
            binary = bin(number)
            count = 0
            for char in binary[2:]:
                if char == '1':
                    count += 1
            if count in dict:
                tmp = dict.get(count)
                tmp.append(number)
                dict[count] = tmp
            else:
                dict[count] = [number]
        # sort by key
        list = sorted(dict.items(),key = lambda i: i[0], reverse = False)
        for tuple in list:
            counted = tuple[1]
            if len(counted) == 1:
                result.append(tuple[1][0])
            else:
                counted.sort()
                for number in counted:
                    result.append(number)
        return result

print(Solution().sortByBits(input))
