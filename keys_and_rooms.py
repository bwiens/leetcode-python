#!/usr/bin/python
# Benjamin Wiens
# Keys and Rooms (https://leetcode.com/problems/keys-and-rooms/)
# Leetcode Accepted

keys_rooms = [[1],[2],[3],[]]
class Solution:
    def canVisitAllRooms(self, rooms):
        stack, keys = [], []
        # always get into room 0, and take care of the keys 
        visited = {0: None}
        for first in rooms[0]:
            if first not in visited:
                visited[first] = None
        stack = rooms[0]
        #print(stack)
        # while there are keys:
        while stack:
            for key in rooms[stack.pop()]:
                print("key", key)
                if key not in visited:
                    visited[key] = None
                    stack.append(key)
        #print("visited", "rooms", visited, rooms)
        #print(stack)
        if len(visited) == len(rooms):
            return True
        else:
            return False
print(Solution().canVisitAllRooms(keys_rooms))
