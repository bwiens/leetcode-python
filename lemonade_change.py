#!/usr/bin/python
bills = [5,5,5,5,20,20,5,5,20,5]
class Solution:
    def lemonadeChange(self, bills):
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if not fives:
                    return False
                tens += 1
                fives -= 1
            else:
                # encounter a 20:
                if fives and tens:
                    fives -= 1
                    tens -= 1
                else:
                    if fives >= 3:
                        fives -= 3
                    else:
                        return False                       
        return True

print(Solution().lemonadeChange(bills))
