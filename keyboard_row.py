#!/usr/bin/python
# Benjamin Wiens
# Keyboard Row (https://leetcode.com/problems/keyboard-row/)

words = ["Hello", "Alaska", "Dad", "Peace"]

class Solution:
    def findWords(self, words):
        result = []
        row1 = {'q': None, 'w': None, 'e': None, 'r': None, 't': None, 'y': None, 'u': None, 'i': None, 'o': None, 'p': None}
        row2 = {'a': None, 's': None, 'd': None, 'f': None, 'g': None, 'h': None, 'j': None, 'k': None, 'k': None, 'l': None}
        row3 = {'z': None, 'x': None, 'c': None, 'v': None, 'b': None, 'n': None, 'm': None}
        row = None
        append = None
        for word in words:
            # reset
            append = True
            row = None
            for letter in word:
                letter = letter.lower()
                if not row:
                    if letter in row1:
                        row = 1
                    elif letter in row2:
                        row = 2
                    else:
                        row = 3
                else:
                    if row == 1:
                        if letter in row2 or letter in row3:
                            append = False
                            break
                    elif row == 2:
                        if letter in row1 or letter in row3:
                            append = False
                            break
                    else:
                        if letter in row2 or letter in row1:
                            append = False
                            break
            if append:
                result.append(word)
        return result

print(Solution().findWords(words))
