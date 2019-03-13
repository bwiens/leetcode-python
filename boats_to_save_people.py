#!/usr/bin/python
#Benjamin Wiens
#Boats to Save People (https://leetcode.com/problems/boats-to-save-people)
#Leetcode Accepted

people = [3,1,7] 
limit = 7
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if len(people) < 2:
            return len(people)
        people.sort(reverse=True)
        #print(people)
        left, right, count = 0, len(people)-1, 0
        while left <= right:                    
            if people[left] <= limit:      
                if people[left] + people[right] <= limit:
                    left += 1
                    right -= 1
                else:
                    left += 1
            count += 1
        return count
print(Solution().numRescueBoats(people, limit))
