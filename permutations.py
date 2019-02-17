#!/usr/bin/python
#Benjamin Wiens
#Permutations (https://leetcode.com/problems/permutations/)
#Leetcode Accepted
input = [-1, 1, 3]
class Solution:
    def permutations(self, string):
        if not len(string):
            return []
        if len(string) == 1:
            return [string]
        result = []
        char = string[0]
        perms = self.permutations(string[1:])
        for perm in perms:
            for i in range(len(perm)+1):
                result.append(perm[:i] +[char]+perm[i:])
        return result
        
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        result = self.permutations(nums)
        return result

print(Solution().permutations(input))
