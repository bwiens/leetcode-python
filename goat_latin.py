#!/usr/bin/python
#Benjamin Wiens
#Goat Latin
#https://leetcode.com/problems/goat-latin/submissions/
#Leetcode Accepted

sentence = "I speak Goat Latin"

class Solution():
    def toGoatLatin(self, s):
        """
        :type s: str
        :rtype: str
        """
        #split into list
        vowels = ["a", "e", "i", "o", "u"]
        s = s.split()
        #enumerate and process each item
        for id, item in enumerate(s):
            #vowels at beginning (rule 1)
            if item[0].lower() in vowels:
                item = item + 'ma'
                #place the item in the list
                s[id] = item
            #consonant at beginning (rule 2)
            if item[0].lower() not in vowels:
                #duplicate first letter to end
                if len(item) > 1:
                    item = item + item[0]
                #strip first letter
                    item = item[1:]
                item = item + 'ma'
                s[id] = item
            #append an per index (rule3)
            item = item + ('a' * (1 + id))
            s[id] = item
        #convert list back to string
        s = ' '.join(s)
        return s

print(Solution().toGoatLatin(sentence))
