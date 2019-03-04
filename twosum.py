#!/usr/bin/python
#Benjamin Wiens
#Two Sum (Non-BruteForce) https://leetcode.com/problems/two-sum
#Leetcode Accepted 
nums = [2, 7, 11, 15]
target = 9

        numdict, x = {}, 0
        #create hashtable
        for index, i in enumerate(nums):
            numdict[i] = index
        for index, i in enumerate(nums):
			#lookup the inverse
            x = target - i
            if x in numdict:
                if index != numdict.get(x):
                    return index, numdict.get(x)

print(Solution().twoSum(nums, target))
