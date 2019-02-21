#!/usr/bin/python
#Benjamin Wiens
#Fruit into Baskets (https://leetcode.com/problems/fruit-into-baskets/)
#Leetcode Accepted

input = [1, 1, 2, 2, 4, 4, 4]
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        weight, max, c = 0, 0, 0
        flowers, flag = {}, False
        if len(set(tree)) < 3:
            return len(tree)
        for index, i in enumerate(tree):
            flowers[i] = None
            weight, c = 1, 1
            while index + c <= (len(tree) -1) and flag == False: 
                if len(flowers) == 1:
                    if tree[index+c] not in flowers:
                        flowers[tree[index+c]] = None
                    weight += 1
                elif len(flowers) == 2:
                    if tree[index+c] in flowers:
                        weight += 1
                    else:
                        flag = True
                c+=1
            if max < weight:
                    max = weight
            flowers, flag = {}, False
        return max

print(Solution().totalFruit(input))
