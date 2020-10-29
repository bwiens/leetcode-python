#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/bulls-and-cows/
secret = "1123"
guess =  "0111"
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        dict = {}
        for index, char in enumerate(secret):
            if guess[index] == char:
                bulls += 1
            else:
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
        for index, char in enumerate(secret):
            #non bull:
            if guess[index] != char and guess[index] in dict:
                    cows += 1
                    dict[guess[index]] -= 1
                    if dict[guess[index]] == 0:
                        del dict[guess[index]]
        return str(bulls)+'A'+str(cows)+'B'

print(Solution().getHint(secret, guess))
