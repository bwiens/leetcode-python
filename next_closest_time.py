#!/usr/bin/python
#Benjamin Wiens
#https://leetfree.com/problems/next-closest-time.html
#Input: "23:59"
#Output: "22:22"

import itertools
time = "23:59"
numbersonly = []
def nextEarliest(string):
    string = list(string)
    #remove colon
    del string[2]
    string = "".join(string)
    #generate all possible products
    result = list(itertools.product(string, repeat = 4))
    nr = 0
    min = int(string)
    for i in result:
        #convert to string
        nr = (''.join(i))
        #filter out invalid times based on 24 hour time format
        if int(str(nr)[0]) <= 2 and int(str(nr)[2]) <= 6 and not (int(str(nr)[0]) == 2 and int(str(nr)[1]) > 4):
            #calculate the difference
            dif = int(nr) - int(string)
            #we cannot have a negative difference
            if dif < 0:
                dif = abs(dif)
                dif = 2400 - dif
            #if the difference is the same it's the original time
            if dif != 0:
                if dif < min:
                    min = dif
                    #add colon
                    lowest = nr[:2] + ':' + nr[2:4]
    return(lowest)

print(nextEarliest(time))
