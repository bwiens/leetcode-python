#!/usr/bin/python
# Benjamin Wiens
# Defanging an IP Address (https://leetcode.com/problems/defanging-an-ip-address/)

input = "1.1.1.1"

class Solution:
    def defangIPaddr(self, address):
        result = ''
        for i in address:
            if i == ".":
                result = result + '[.]'
            else:
                result = result + i
        return result

print(Solution().defangIPaddr(input))
