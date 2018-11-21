#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/bulls-and-cows/
secret = "1123"
guess =  "0111"

class Solution:
    def getHint(self, secret, guess):
        """
        :param secret: str
        :param guess: str
        :return: str
        """
        bulls = 0
        cows = 0
        #create hash tables with incremented idex
        guess_map = dict(enumerate(guess))
        secret_map = dict(enumerate(secret))
        #find the ones (bulls) in position
        for key, value in secret_map.items():
            if guess_map.get(key)  == value:
                #overwrite value
                secret_map[key] = 'X'
                guess_map[key] = 'A'
                bulls += 1
        for key, value in secret_map.items():
            for key2, value2 in guess_map.items():
                if value == value2:
                    #overwrite value
                    guess_map[key2] = 'Z'
                    cows += 1
                    break
        return str(bulls) + 'A' + str(cows) + 'B'
print(Solution().getHint(secret, guess))
