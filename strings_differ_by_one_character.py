#!/usr/bin/python

dict = ["abcd","acbd", "aacd"]

class Solution:
    def differByOne(self, dict):
        for index, key in enumerate(dict):
            for index2, key2 in enumerate(dict):
                if index != index2:
                    if len(key) == len(key2):
                        foundOne = False
                        for index, char in enumerate(key):
                            if char != key2[index]:
                                if not foundOne:
                                    foundOne = True
                                else:
                                    break
                            if index == len(key) -1 and foundOne:
                                return True
        return False
                        
print(Solution().differByOne(dict))                            
                            
