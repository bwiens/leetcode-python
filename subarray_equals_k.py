#!/usr/bin/python
# Benjamin Wiens
# Subarray Sum Equals K (https://leetcode.com/problems/subarray-sum-equals-k/)
# Leetcode Accepted

nums = [1, 1, 1]
k = 2

class Solution:
    def subarraySum(self, nums, k):
        # trick we intiialize dict with 0 = 1 in case num - k = 0. trick
        dict, count = {0: 1}, 0
        rolling = 0
        for number in nums:
            # we NEVER check the number only. we ALWAYS check rolling or rolling - k
            rolling += number
            # check if rolling - k is in dict 
            if rolling - k in dict:
                count += dict.get(rolling-k)
            if rolling not in dict:
                dict[rolling] = 1
            else:
                dict[rolling] += 1
        return count

print(Solution().subarraySum(nums,k))
