#!/usr/bin/python
# Benjamin Wiens
# Rotate String ()

A = "abcde"
B = "cdeab"

class Solution:
    def rotateString(self, A, B):
        if not A and not B:
            return True
        string = A
        for i in range(len(A)):
            string += A[i]
            if string[i+1:] == B:
                return True
        return False

print(Solution().rotateString(A,B))
