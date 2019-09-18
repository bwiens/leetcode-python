#!/usr/bin/python
# Benjamin Wiens
# Campus Bikes (https://leetcode.com/problems/campus-bikes/)

workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]

class Solution:
    def assignBikes(self, workers, bikes):
        distances = []
        # calculate manhattan distance of all combinations
        for w_index, worker in enumerate(workers):
            for b_index, bike in enumerate(bikes):
                distance = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                distances.append((distance, w_index, b_index))
        # sort by manhattan distance
        distances.sort()
        bikes_taken = []
        result = ['X'] * len(workers)
        for distance, w_index, b_index in distances:
            if result[w_index] == 'X' and b_index not in bikes_taken:
                result[w_index] = b_index
                # mark bike as taken
                bikes_taken.append(b_index)
        return result

print(Solution().assignBikes(workers,bikes))
