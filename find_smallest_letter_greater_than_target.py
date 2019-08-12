#!/usr/bin/python
# Benjamin Wiens
# Find Smallest Letter Greater Than Target

letters = ["c","f","j"]
k = "a"

class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        for char in letters:
            if char > target:
                return char
        #else wrap around and pick first
        return letters[0]

print(Solution().nextGreatestLetter(letters,k))
