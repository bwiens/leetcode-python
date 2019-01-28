#!/usr/bin/python
#Benjamin Wiens
#Letter Combinations of a Phone Number (https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
#Leetcode Accepted
import itertools
input = "23"
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result, result_f = [], []
        digits = list(digits)
        dict = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g","h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        #create list of valid letters
        for index, i in enumerate(digits):
            result.append(dict[int(i)])
        #create cartesian product and format
        for i in (list(itertools.product(*result))):
            result_f.append("".join(i))
        return result_f

print(Solution().letterCombinations(input))
