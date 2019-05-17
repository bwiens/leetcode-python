#!/usr/bin/python
# Benjamin Wiens
# Unique Morse Code Words (https://leetcode.com/problems/unique-morse-code-words/)
# Leetcode Accepted

words = ["gin", "zen", "gig", "msg"]
class Solution:
    def uniqueMorseRepresentations(self, words):
        mdict = {"a": ".-","b" : "-...","c" : "-.-.","d" : "-..","e" : ".", "f": "..-.","g": "--.","h": "....","i": "..", "j": ".---","k": "-.-", "l" : ".-..", "m": "--","n" : "-.","o": "---","p": ".--.","q": "--.-","r": ".-.", "s": "...","t": "-","u": "..-","v": "...-","w": ".--","x": "-..-", "y": "-.--", "z": "--.."}
        tmp = ''
        result = []
        for word in words:
            for letter in word:
                tmp += mdict.get(letter)
            result.append(tmp)
            tmp = ''
        return len(set(result))

print(Solution().uniqueMorseRepresentations(words))
