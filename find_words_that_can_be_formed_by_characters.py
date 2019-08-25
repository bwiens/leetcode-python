#!/usr/bin/python
# Benjamin Wiens
# Find Words that can be Formed by Characters (https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)

words = ["cat","bt","hat","tree"]
chars = "atach"
import copy
class Solution:
    def countCharacters(self, words, chars) -> int:
        hmap = {}
        result = 0
        for char in chars:
            if char in hmap:
                hmap[char] += 1
            else:
                hmap[char] = 1
        for word in words:
            all_found = True
            hmap2 = copy.deepcopy(hmap)
            for char in word:
                if char not in hmap2:
                    all_found = False
                    break
                else:
                    x = hmap2.get(char)
                    if x == 1:
                        del hmap2[char]
                    else:
                        hmap2[char] -= 1
            if all_found:
                result += len(word)
        return result

print(Solution().countCharacters(words,chars))
