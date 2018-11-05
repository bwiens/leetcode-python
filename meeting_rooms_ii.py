#!/usr/bin/python
#Benjamin Wiens
#Meeting Rooms II (https://leetfree.com/problems/meeting-rooms-ii.html)

#This is still brainstorming, not sure if viable
slots = [[0, 30],[15, 20], [5, 10]]

slots.sort()

print(slots)

def roomCount(times):
    i = 1
    #intitial room for first meeting
    c = 1
    #compare end times
    for i in range(len(slots)):
        if int(slots[i-1][1]) > int(slots[i][1]):
            c= c + 1
    return c

print(roomCount(slots))
