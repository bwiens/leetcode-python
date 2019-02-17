#!/usr/bin/python
#Benjamin Wiens
#Fizz-Buzz (https://leetcode.com/problems/fizz-buzz/)
#Leetcode Accepted
input = 15

class Solution:
    def fizzBuzz(self, n: 'int') -> 'List[str]':
        result = []
        if not n:
            return []
        #start at one, end +1 after n
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

print(Solution().fizzBuzz(input))
