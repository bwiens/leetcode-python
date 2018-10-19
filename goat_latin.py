#!/usr/bin/python
#Benjamin Wiens
#Goat Latin
#Rule1: If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
#   For example, the word 'apple' becomes 'applema'.
#Rule2: If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
#   For example, the word "goat" becomes "oatgma".
#Rule3: Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#   For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

sentence = "I speak Goat Latin"
vowels = ["a", "e", "i", "o", "u"]

class Solution():
    def toGoatLatin(self, s):
        """
        :type s: str
        :rtype: str
        """
        #split into list
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
                item = item + item[0]
                #strip first letter
                item = item.lstrip(item[0])
                item = item + 'ma'
                s[id] = item
            #append an per index (rule3)
            item = item + ('a' * (1 + id))
            s[id] = item
        #convert list back to string
        s = ' '.join(s)
        return s

print(Solution().toGoatLatin(sentence))
