#!/usr/bin/python
#Benjamin Wiens
#Given a string, find the length of the longest substring T that contains at most k distinct characters.
#(https://leetfree.com/problems/longest-substring-with-at-most-k-distinct-characters.html)

#For example, Given s = “eceba” and k = 2,
#T is "ece" which its length is 3.

s = "eceba"
k = 2
def longestsub(string,chars):
    """
    :param string: str
    :param chars: num
    :return: str
    """
    s = ""
    maximum = ""
    for i in string:
       s += i
       if (len(set(s))) <= k:
                if len(s) > len(maximum):
                    maximum = s
       if (len(set(s))) > k:
           s = s[1:]
    return maximum

print(longestsub(s, k))


