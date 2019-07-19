#!/usr/bin/python
# Benjamin Wiens
# Reorder Log Files (https://leetcode.com/problems/reorder-log-files/)

files = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

class Solution:
    def reorderLogFiles(self, logs):
        letterlogs, digitlogs, result = [], [], []
        for log in logs:
            try:
                test = int(log[-1])
                #preserve original order for digit logs
                digitlogs.append(log)
            except:
                #split letter logs to sort lexographically
                id, rest = log.split(' ', 1)
                letterlogs.append([id, rest])
        #sort
        letterlogs = sorted(letterlogs, key = lambda x: (x[1], x[0]))
        #join
        for log in letterlogs:
            result.append(' '.join(log))
        #extend
        result.extend(digitlogs)
        return result

print(Solution().reorderLogFiles(files))
