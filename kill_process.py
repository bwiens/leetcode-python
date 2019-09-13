#!/usr/bin/python
# Benjamin Wiens
# Kill Process (https://leetcode.com/problems/kill-process/)

pid = [1,3,10,5]
ppid = [3,0,5,3]
kill = 5
from collections import deque
class Solution:
    def killProcess(self, pid, ppid, kill):
        # map parents to their children (aw, how cute)
        hmap, result = {}, []
        for index, parent in enumerate(ppid):
            # if there's no result (yet), it creates an empty list as result
            hmap[parent] = hmap.get(parent, []) 
            hmap[parent].append(pid[index])
        queue = deque([kill])
        while queue:
            to_kill = queue.popleft()
            result.append(to_kill)
            children = hmap.get(to_kill, [])
            queue.extend(children)
        return result
print(Solution().killProcess(pid,ppid,kill))
