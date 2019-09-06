#!/usr/bin/python
# Benjamin Wiens
# Candy Crush (https://leetcode.com/problems/candy-crush)

input = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

from collections import deque
class Solution:
    def candyCrush(self, board):
        crushed = True
        while crushed:
            crushlist = []
            count = 0
            nextnr = None
            crushed = False
            # gather crushes horizontally:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        continue
                    # check neighbors going forward
                    count = 1
                    current = board[i][j]
                    c = 1
                    if j + c <= len(board[0])-1:
                        nextnr = board[i][j+c]
                    if current != nextnr:
                        continue
                    while j+c <= len(board[0])-1 and nextnr == current:
                        count += 1
                        c += 1
                        if j + c <= len(board[0])-1:
                            nextnr = board[i][j+c]
                    if count >= 3:
                        for k in range(count):
                            #board[i][j+k] = 0
                            crushlist.append([i,j+k])
                            crushed = True
            # gather crushes vertically
            for i in range(len(board[0])):
                for j in range(len(board)):
                    if board[j][i] == 0:
                        continue
                    # check neighbors going forward
                    count = 1
                    current = board[j][i]
                    c = 1
                    if j + c <= len(board)-1:
                        nextnr = board[j+c][i]
                    if current != nextnr:
                        continue
                    while j+c <= len(board)-1 and nextnr == current:
                        count += 1
                        c += 1
                        if j + c <= len(board)-1:
                            nextnr = board[j+c][i]
                    if count >= 3:
                        for k in range(count):
                            crushlist.append([j+k,i])
                            crushed = True
            # crush based on crush list
            for crush in crushlist:
                board[crush[0]][crush[1]] = 0
            # apply gravity
            for i in range(len(board[0])):
                column = deque()
                zero_count = 0
                for j in range(len(board)):
                    if board[j][i] == 0:
                        zero_count += 1
                        continue
                    column.append(board[j][i])
                for k in range(len(board)):
                    if zero_count > 0:
                        board[k][i] = 0
                        zero_count -= 1
                    else:
                        board[k][i] = column.popleft() 
        return board

print(Solution().candyCrush(input))
