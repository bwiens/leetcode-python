#!/usr/bin/python
#Benjamin Wiens
#Unique Email Addresses (https://leetcode.com/problems/unique-email-addresses)
#Leetcode Accepted
import re
Input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Solution:
    def numUniqueEmails(self, emails):
        """
        :param emails: List[str]
        :return: int
        """
        result = []
        c = 0
        address = ""
        for i in emails:
            #regex to ignore +strings
            i = re.sub(r'\+[^@]*(?=@)', '', i)
            for index, k in enumerate(i):
                if k != "." and k != "@":
                    address += k
                    #after @ don't ignore dots
                if k == "@":
                    for z in i[index:]:
                        address += z
                        z=""
                        k=""
                    result.append(address)
                    address = ""
                    break
        c = len(set(result))
        return c

print(Solution().numUniqueEmails(Input))
