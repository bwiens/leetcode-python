#!/usr/bin/python
#Benjamin Wiens
#Ransom Note (https://leetcode.com/problems/ransom-note)
#Leetcode Accepted
#O(n+m) time
i1 = "release the hostage now"
i2 = "release the hostage"

class Solution:
    def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
        magazine_map = {}
        x = 0
        for i in magazine:
            if i in magazine_map:
                magazine_map[i] = magazine_map.get(i) +1
            else:
                magazine_map[i] = 1
        for i in ransomNote:
            if i not in magazine_map:
                return False
            else:
                x = magazine_map.get(i)
                if x == 0:
                    return False
                else:
                    magazine_map[i] = x-1
        return True
                
print(Solution().canConstruct(i1, i2))        
