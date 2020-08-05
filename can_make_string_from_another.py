#!/usr/bin/python

a = 'XY'
b = 'XXXYYY'

def canMake(string1, string2):
    length = len(string2)
    reduced = string2.replace(string1, '')
    # found everything
    if len(reduced) == 0:
        return True
    # found nothing
    elif len(reduced) == length:
        return False
    else:
        return canMake(string1, reduced)


print(canMake(a, b))
