#!/usr/bin/python

input = ["BCA","CAB","CBA","ABC","ACB","BAC"]
class Solution:
    def rankTeams(self, votes):
        dict = {}
        result = ''
        for vote in votes:
            for index, char in enumerate(vote):
                if char not in dict:
                    dict[char] = [0] * len(votes[0]) 
                dict[char][index] -= 1
        sort = sorted(dict.items(), reverse=False, key=lambda k: (k[1],k[0]))
        for l in sort:
            result += l[0]
        return result

print(Solution().rankTeams(input))
