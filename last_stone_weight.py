#/!usr/bin/python
# Benjamin Wiens
# Last Stone Weight (https://leetcode.com/problems/last-stone-weight/submissions/)
# Leetcode Accepted 

stones = [3,7,2]
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #the trick is to create a minheap after negating the numbers
        for index, i in enumerate(stones):
            stones[index] = i * -1
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            #print(stones)
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 == stone2:
                continue
            else:
                newstone = stone1-stone2
                heapq.heappush(stones, newstone)
        if stones:
            return abs(stones[0]) 
        else:
            return 0

print(Solution().lastStoneWeight(stones))
#O(nlogn)
