#!/usr/bin/python
#Benjamin Wiens
#Best Subway Seat
#Return index of best subway seat (the most "free" one). 0 = free
import sys
seats = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]

dict = {}

def bestseats(seats):
    count, max = 0, -sys.maxsize -1
    start = -1
    end = -1
    for index, i in enumerate(seats):
        count, 0
        if i == 0:
            while seats[index+count] != 1:
                count += 1
            if max < count:
                    max = count
                    start = index
                    end = index + count
            count = 0
    return[(start+ end)//2]

print(bestseats(seats))
