#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/candy/

input = [1, 2, 2]

class Solution:
    def candy(self, ratings):
        """
        :param ratings: List[int]
        :return: int
        """
        c=0
        for index, i in enumerate(input):
            #the beginning
            if index == 0:
                if i > input[index + 1]:
                    c += 2
                else:
                    c += 1
            #the end
            elif index == (len(input)-1):
                if input[index - 1 ] >= i:
                    c += 1
                else:
                    c += 2
            #has 2 neighbors
            else:
                if ((input[index-1] < i) or (input[index+1] < i)):
                    c += 2
                else:
                    c += 1
        return c

print(Solution().candy(input))
