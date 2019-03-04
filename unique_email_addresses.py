#!/usr/bin/python
#Benjamin Wiens
#Unique Email Addresses (https://leetcode.com/problems/unique-email-addresses)
#Leetcode Accepted
import re
input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Solution:
    def numUniqueEmails(self, emails):
        atflag, plusflag = False, False
        mail = ''
        result = []
        for email in emails:
            for i in email:
                if atflag == False:
                    if i == '@':
                        mail += '@'
                        atflag = True
                    elif i == "+":
                        plusflag = True
                    elif i != "." and plusflag == False:
                            mail += i
                else:
                    mail += i
            result.append(mail)
            mail = ''
            atflag, plusflag = False, False
        return len(set(result))

print(Solution().numUniqueEmails(input))
