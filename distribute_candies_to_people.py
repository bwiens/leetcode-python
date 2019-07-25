#!/usr/bin/python
# Benjamin Wiens
# Distribute Candies to People (https://leetcode.com/problems/distribute-candies-to-people)

candies = 7
people = 4

class Solution:
    def distributeCandies(self, candies, num_people):
        result = [0] * num_people
        i = 0
        n_candies = 1
        while candies:
            if candies - n_candies >= 0:
                candies -= n_candies
            else:
                break
            result[i] = result[i] + n_candies
            #increment by 1 to give each following person more
            n_candies += 1
            i += 1
            if i == len(result):
                i = 0
        if candies > 0 : result[i] = result[i] + candies
        return result

print(Solution().distributeCandies(people, candies))
