#!/usr/bin/python
#Benjamin Wiens
#https://leetcode.com/problems/replace-words/description/

input = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
result = []
result_str = ''

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :param dict: List[str]
        :param sentence: str
        :return: str
        """
        #convert to list
        sentence_list = sentence.split()
        #check if words are part of the list
        for i in sentence_list:
            #use replacement instead
            if i[:3] in input:
                result.append(i[:3])
            #use original
            else:
                result.append(i)
            result_str = ' '.join(result)
        return result_str

print(Solution().replaceWords(input, sentence))
