#!/usr/bin/python
# Benjamin Wiens
# Queens That Can Attack the King (https://leetcode.com/problems/queens-that-can-attack-the-king/)

queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
king = [3,3]

class Solution:
    def queensAttacktheKing(self, queens, king):
        result = []
        board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        board[king[0]][king[1]] = 'K'
        for queen in queens:
            board[queen[0]][queen[1]] = 'Q'
        for rindex, row in enumerate(board):
            for cindex, column in enumerate(row):
                if column == 'K':
                    # right
                    j = cindex + 1
                    while j < len(board[0]):
                        if board[rindex][j] == 'Q':
                            result.append([rindex,j])
                            break
                        else:
                            j += 1
                    # left
                    j = cindex - 1
                    while j >= 0:
                        if board[rindex][j] == 'Q':
                            result.append([rindex, j])
                            break
                        else:
                            j -= 1
                    # down
                    j = rindex + 1
                    while j < len(board):
                        if board[j][cindex] == 'Q':
                            result.append([j,cindex])
                            break
                        else:
                            j += 1
                    # up
                    j = rindex - 1
                    while j >= 0:
                        if board[j][cindex] == 'Q':
                            result.append([j,cindex])
                            break
                        else:
                            j -= 1
                    #down-right
                    j = rindex + 1
                    k = cindex + 1
                    while j < len(board) and k < len(board[0]):
                        if board[j][k] == 'Q':
                            result.append([j,k])
                            break
                        else:
                            j += 1
                            k += 1
                    # down-left
                    j = rindex + 1
                    k = cindex - 1
                    while j < len(board) and k >= 0:
                        if board[j][k] == 'Q':
                            result.append([j,k])
                            break
                        else:
                            j += 1
                            k -= 1
                    #up-right
                    j = rindex - 1
                    k = cindex + 1
                    while j >= 0 and k < len(board[0]):
                        if board[j][k] == 'Q':
                            result.append([j,k])
                            break
                        else:
                            j -= 1
                            k += 1
                    #up-left
                    j = rindex - 1
                    k = cindex - 1
                    while j >= 0 and k >= 0:
                        if board[j][k] == 'Q':
                            result.append([j,k])
                            break
                        else:
                            j -= 1
                            k -= 1
        return result

print(Solution().queensAttacktheKing(queens,king))
