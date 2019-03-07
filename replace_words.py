#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/replace-words/description/

input = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

class Solution:
    def replaceWords(self, dict, sentence):
        sentence_list = sentence.split()
        result = []
        for i in sentence_list:
            c, found = 1, False
            #loop over the word, find the shortest match
            while c < len(i) and found == False:
                if i[:c] in dict:
                    found = True
                    result.append(i[:c])
                    break
                c+=1
            #if no match has been found
            if found == False:
                result.append(i)
        return ' '.join(result)

print(Solution().replaceWords(input, sentence))
