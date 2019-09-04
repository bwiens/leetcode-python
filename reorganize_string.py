#!/usr/bin/python
# Benjamin Wiens
# Reorganize String (https://leetcode.com/problems/reorganize-string/)

from collections import Counter
string = "gpneqthatplqrofqgwwfmhzxjddhyupnluzkkysofgqawjyrwhfgdpkhiqgkpupgdeonipvptkfqluytogoljiaexrnxckeofqojltdjuujcnjdjohqbrzzzznymyrbbcjjmacdqyhpwtcmmlpjbqictcvjgswqyqcjcribfmyajsodsqicwallszoqkxjsoskxxstdeavavnqnrjelsxxlermaxmlgqaaeuvneovumneazaegtlztlxhihpqbajjwjujyorhldxxbdocklrklgvnoubegjrfrscigsemporrjkiyncugkksedfpuiqzbmwdaagqlxivxawccavcrtelscbewrqaxvhknxpyzdzjuhvoizxkcxuxllbkyyygtqdngpffvdvtivnbnlsurzroxyxcevsojbhjhujqxenhlvlgzcsibcxwomfpyevumljanfpjpyhsqxxnaewknpnuhpeffdvtyjqvvyzjeoctivqwann"

class Solution:
    def reorganizeString(self, S):
        # find most frequent character
        hmap = Counter(S)
        result, leftovers = [], []
        most = None
        for key, value in hmap.most_common():
            # break if impossible to not place adjacently 
            if value > (len(S)+1)/2:
                return ""
            if not most:
                most = key
                most_v = value
                continue
            # create a leftovers-stack
            for i in range(value):
                leftovers.append(key)
		# create a result array of length S
        result = len(S) * [0]
        # fill even result indices with most frequent, then with leftovers
        for i in range(0,len(result),2):
            if most_v:
                result[i] = most
                most_v -= 1
            elif leftovers:
                result[i] = leftovers.pop()
            else:
                break
        # fill odd result indices with leftovers
        for i in range(1,len(result), 2):
                result[i] = leftovers.pop()
        return ''.join(result)

print(Solution().reorganizeString(string))
