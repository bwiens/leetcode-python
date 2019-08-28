#!/usr/bin/python
# Benjamin Wiens
# Available Captures for Rook (https://leetcode.com/problems/available-captures-for-rook/)

board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

class Solution:
    def numRookCaptures(self, board):
        row_length = len(board)
        column_length = len(board[0])
        count = 0
        for rid, row in enumerate(board):
            for cid, column in enumerate(row):
                if column == "R":
                    #up
                    c = 1
                    while rid - c >= 0:
                        if board[rid-c][cid] =="p":
                            count += 1
                            break
                        if board[rid-c][cid] =="B":
                            break
                        c += 1
                    #down
                    c = 1
                    while rid + c < row_length:
                        if board[rid+c][cid] =="p":
                            count += 1
                            break
                        if board[rid+c][cid] =="B":
                            break
                        c += 1
                    #right
                    c = 1
                    while cid + c < column_length:
                        if board[rid][cid+c] =="p":
                            count += 1
                            break
                        if board[rid][cid+c] =="B":
                            break
                        c += 1
                    #left
                    c = 1
                    while cid - c >= 0:
                        if board[rid][cid-c] =="p":
                            count += 1
                            break
                        if board[rid][cid-c] =="B":
                            break
                        c += 1
        return count

print(Solution().numRookCaptures(board))
