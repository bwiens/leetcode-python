#!/usr/bin/python
#Benjamin Wiens
#Iterative Palindrome Detector
#Consider only alphanumeric characters (case insensitve)

import re

palin = "A man, a plan, a canal: Panama"
palin2 = "race a car"


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove non-alphanumeric characters using regular expression
        s = re.sub (r'\W+', '', s)
        #print(s)
        # split into halves
        palin_half = len (s) // 2
        first_half = s[:palin_half]
        second_half = list (reversed (s[palin_half:]))
        c = 0
        #iterate through string and compare
        for i in range(len(first_half)):
            #print(first_half[i])
            #print(second_half[i])
            if first_half[i].lower() != second_half[i].lower():
                c += 1
        if c == 0:
            #print("Palindrome detected")
            return True
        else:
            #print("Not a Palindrome")
            return False

print(Solution().isPalindrome(palin))
print(Solution().isPalindrome(palin2))
#Since we have one for loop, the time complexity is O(n)
