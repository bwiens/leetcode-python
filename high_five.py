#!/usr/bin/python
# Benjamin Wiens
# High Five (https://leetcode.com/problems/high-five/)
# Leetcode Accepted

scores = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

class Solution:
    def highFive(self, items):
        count = {}
        result = []
        tmp = 0
        items.sort(reverse=True)
        #print(items)
        for score in items:
            if score[0] not in count:
                count[score[0]] = 1
                tmp += score[1]
            else:
                if count.get(score[0]) < 5:
                    count[score[0]] += 1
                    tmp += score[1]
                    if count.get(score[0]) == 5:
                            tmp = tmp // 5
                            result.append([score[0],tmp])
                            tmp = 0
        return result[::-1]

print(Solution().highFive(scores))

#O(nlogn) time
