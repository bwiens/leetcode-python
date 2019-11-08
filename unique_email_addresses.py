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
        eSet = set()
        at = True
        for email in emails:
            split = email.split('@')
            first = ''
            for e in split[0]:
                if e == '.':
                    continue
                elif e == '+':
                    break
                else:
                    first += e
            result = first + '@' + split[1]
            if result not in eSet:
                eSet.add(result)
        return len(eSet)

print(Solution().numUniqueEmails(input))
