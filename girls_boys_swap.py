#!/usr/bin/python
#Benjamin Wiens
#In a school, the students were playing a game.Initially everyone is standing
#in a circular path in the school lawn.The student at index 1 is standing next to
#student at index n and before the student at index 2.All the girls need to stand
#together to win the game.The girls had influencial power to influence the boys to
#swap the positions.Help the Girls decide the minimum number of swaps they have to do
#so that all of them stand together.
#example: BBGBGBG
#BBBBGGG
#answer=1

s = 'BBGBGBGGB'

def minSwaps(s):
    """
    :param s: str
    :return: int
    """
    c, min, x = 0, 0, 0
    #count the number of boys
    for i in s:
        if i == 'B':
            c += 1
    min = int(s.count('B', 0, 3))
    for index, i in enumerate(s):
        if index + c <= len(s):
            x = int(s.count('B',index,index+c))
            if x < min:
                min = x
    return min



print(minSwaps(s))

#Runetime is O(n). Initially find the number of total boys in the string that is 4 in this case.
#Then consider all the windows of size 4 each and the find the number of girls in that ,take the minimum of them you'll have the answer
