#!/usr/bin/python
# Benjamin Wiens
# Unique Email Addresses (cleaner version https://leetcode.com/problems/unique-email-addresses)
# Leetcode Accepted

input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = []
        first = ''
        for email in emails:
            #seperate two parts (befoer and after @)
            splits = email.split('@')
            for i in splits[0]:
                if i == ".":
                    continue
                elif i == "+":
                    break
                else:
                    #concatenate
                    first = first + i
            result.append(first + '@' + splits[1])
            first = ''
        return len(set(result))

print(Solution().numUniqueEmails)
