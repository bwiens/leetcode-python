#!/usr/bin/python
# Benjamin Wiens
# Fruit Into Basket (https://leetcode.com/problems/fruit-into-baskets/)
# Leetcode Accepted, using a dictionary
fruit = [1,2,3,2,2]

class Solution(object):
    def totalFruit(self, tree):
        if len(tree) <= 2:
            return len(tree)
	# j counter
        j = 0
        maximum = 2
        count = {}
        # iterate over tree, and keep a dictionary. Once len(dict) > 2, we move j to the right until len(dict) == 2
        for index, t in enumerate(tree):
            if t in count:
                count[t] += 1
            else:
                count[t] = 1
            while len(count) > 2:
                # increment j pointer
                count[tree[j]] -= 1
                if count[tree[j]] == 0:
                    del count[tree[j]]
                j += 1
            maximum = max(index-j+1, maximum)
        return maximum
print(Solution().totalFruit(fruit))
