#!/usr/bin/python
# Benjamin Wiens
# Sum of Even Numbers After Queries (https://leetcode.com/problems/sum-of-even-numbers-after-queries)
# Leetcode Accepted 

A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

class Solution:
    def sumEvenAfterQueries(self, A, queries):
        result = []
        tmp_sum = 0
        #get original sum
        for number in A:
                if number % 2 == 0:
                    tmp_sum += number
        for i in queries:
            og = A[i[1]]
            #remove from sum if even
            if og % 2 == 0:
                tmp_sum -= A[i[1]]
            A[i[1]] += i[0]
            #add to sum if even
            if A[i[1]] % 2 == 0:
                tmp_sum += A[i[1]]
            result.append(tmp_sum)
        return result

print(Solution().sumEvenAfterQueries(A, queries))
