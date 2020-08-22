#!/usr/bin/python

dict = ["abcd","acbd", "aacd"]

class Solution:
    def differByOne(self, dict):
        combos = set()
        for key in dict:
            for i in range(len(key)):
                combo = key[:i] + '*' + key[i+1:]
                if combo in combos:
                    return True
                combos.add(combo)
        return False

print(Solution().differByOne(dict))                            
                            
