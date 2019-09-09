#!/usr/bin/python
# Benjamin Wiens
# All Paths From Source to Target (https://leetcode.com/problems/all-paths-from-source-to-target/)

input = [[1,2], [3], [3], []] 

class Solution:
    def allPathsSourceTarget(self, graph):
        def traverse(index, q):
            # we found a path to node n-1
            if index == len(graph) -1:
                result.append(q)
            # travel along the nodes
            for i in graph[index]:
                traverse(i, q + [i])
            return result
        result = []
        traverse(0, [0])
        return result

print(Solution().allPathsSourceTarget(input))
