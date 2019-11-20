#!/usr/bin/python
#Benjamin Wiens
#Unique Email Addresses (https://leetcode.com/problems/unique-email-addresses)
#Leetcode Accepted
import re
input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            first, second = email.split('@')
            tmp = ''
            for char in first:
                if char == "+":
                    break
                elif char == ".":
                    continue
                else:
                    tmp = tmp + char
            result.add(tmp + '@' + second)
        return len(result)
print(Solution().numUniqueEmails(input))
