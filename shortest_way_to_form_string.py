#!/usr/bin/python
# Benjamin Wiens
# Shortest Way to Form String (https://leetcode.com/problems/shortest-way-to-form-string/)

source = "abc"
target = "abcbc"

class Solution:
    def shortestWay(self, source, target):
        found = True
        sp, tp, result = 0, 0, 0
        while tp < len(target):
            # start from beginning of source each time
            # we inch ourselves closer, greedily. as long as we can progress tp moves forward and we find something
            # O(n*m)
            sp = 0
            found = False
            while sp < len(source) and tp < len(target):
                if source[sp] == target[tp]:
                    sp += 1
                    tp += 1
                    found = True
                else:
                    # if not a match move source
                    sp += 1
            if found:
                result += 1
            else:
                return -1
        return result

print(Solution().shortestWay(source, target))
