#!/usr/bin/python
# Benjamin Wiens
# Partition Labels (https://leetcode.com/problems/partition-labels/)

S = "ababcbacadefegdehijhklij"

class Solution:
    def partitionLabels(self, S):
        hmap, result = {}, []
        maximum_index, count = 0, 0
        for index, char in enumerate(S):
            hmap[char] = index
        for index, char in enumerate(S):
            count += 1
            maximum_index = max(maximum_index,hmap[char])
            if index == maximum_index:
                result.append(count)
                maximum_index, count = 0, 0
        return result

print(Solution().partitionLabels(S))
