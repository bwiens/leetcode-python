#!/usr/bin/python
#Benjamin Wiens
# 3Sum (https://leetcode.com/problems/3sum/)
# Leetcode Accepted
input = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums: 'List[int]'):
        c, numbercount = 0, 0
        zero = []
        hash = {}
        if set(nums) == {0}:
            if len(nums) < 3:
                return []
            else:
                return [0,0,0]
	#create a hashtable with number occurrences as values
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        for index, i in enumerate(nums):
            for jindex, j in enumerate(nums):
                #create pairs, lookup their inverse in the hashtable
                # make sure not to use duplicates by checking the count
                if index != jindex:
                    pair = i + j
                    if -pair in hash:
                        numbercount = hash.get(-pair)
                        if numbercount >= [i, j, -pair].count(-pair):
                            tmp = sorted([i,j, -pair])
                            zero.append(tmp)
        return [list(x) for x in set(tuple(x) for x in zero)]

print(Solution().threeSum(input))
