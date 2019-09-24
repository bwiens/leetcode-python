#!/usr/bin/python
# Benjamin Wiens
# Can Place Flowers (https://leetcode.com/problems/can-place-flowers/)

flowerbed = [1,0,0,0,1]
n = 2

class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1 == n
        count = 0
        for i in range(len(flowerbed)):
            if count >= n:
                return True
            if i == 0:
                if flowerbed[i] == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count +=1 
            else:
                if flowerbed[i] == 0 and i < len(flowerbed) -1:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1
                elif i == len(flowerbed) -1 and flowerbed[i] == 0:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        count += 1
        if count >= n:
            return True
        else:
            return False

print(Solution().canPlaceFlowers(flowerbed,n))                        
