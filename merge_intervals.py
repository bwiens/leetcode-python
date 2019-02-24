#!/usr/bin/python
#Benjamin Wiens
#Merge Intervals
#Append each element (sorted) to the result list
#Merge when appropriate, otherwise append

input = [[1,4],[0,2],[2,3],[3, 4], [7,9]]

def mergintervals(intervals):
    result = []
    intervals = sorted(intervals)
    #print(intervals)
    for index, i in enumerate(intervals):
        if index == 0:
            result.append(i)
        else:
            if i[0] <= result[-1][1]:
                tmp = result[-1]
                result.pop()
                result.append([tmp[0],i[1]])
            else:
                result.append(i)
    return(result)

print(mergintervals(input))
