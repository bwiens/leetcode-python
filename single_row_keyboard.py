#!/usr/bin/python
# Benjamin Wiens
# Single-Row Keyboard (https://leetcode.com/problems/single-row-keyboard/)

keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"

class Solution:
    def calculateTime(self, keyboard, word) -> int:
        hmap = {}
        for index, char in enumerate(keyboard):
            hmap[char] = index
        time = 0
        current_index = 0
        for char in word:
            time += abs(current_index - hmap.get(char))
            current_index = hmap.get(char)
        return time

print(Solution().calculateTime(keyboard,word))
