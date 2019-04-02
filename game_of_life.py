#!/usr/bin/python
# Benjamin Wiens
# Game of Life (https://leetcode.com/problems/game-of-life/)
# Leetcode Accepted

import copy
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        livecount = 0
        #The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances)
        boardcopy = copy.deepcopy(board)
        #create a copy, keep looking at the copy, but do change the original
        for rid, row in enumerate(boardcopy):
            for cid, column in enumerate(row):
                livecount = 0
                # calculate the live count
                # up
                if rid-1 >= 0:
                    if boardcopy[rid-1][cid] == 1:
                        livecount += 1
                # down
                if rid+1 <= len(boardcopy) - 1:
                    if boardcopy[rid+1][cid] == 1:
                        livecount += 1
                # left
                if cid-1 >= 0:
                    if boardcopy[rid][cid-1] == 1:
                        livecount += 1
                # right
                if cid+1 <= len(boardcopy[0]) -1:
                    if boardcopy[rid][cid+1] == 1:
                        livecount += 1
                # top right diag
                x= rid-1
                if cid+1 <= len(boardcopy[0]) - 1 and rid - 1 >= 0:
                    if boardcopy[rid-1][cid+1] == 1:
                        livecount += 1
                # top left diag
                if cid-1 >= 0 and rid-1 >= 0:
                    if boardcopy[rid-1][cid-1] == 1:
                        livecount += 1
                # bottom right diag
                if cid+1 <= len(boardcopy[0])-1 and rid+1 <= len(boardcopy) -1:
                    if boardcopy[rid+1][cid+1] == 1:
                        livecount += 1
                # bottom left diag
                if cid-1 >= 0 and rid+1 <= len(boardcopy)-1:
                    if boardcopy[rid+1][cid-1] == 1:
                        livecount += 1
                # apply game of life rules
                # rule 1 and 3
                if column == 1:
                    if livecount < 2 or livecount > 3:
                        board[rid][cid] = 0
                # rule 2
                if column == 1:
                    if livecount in [2,3]:
                        board[rid][cid] = 1
                # rule 4
                if column == 0 and livecount == 3:
                    board[rid][cid] = 1
        return board
print(Solution().gameOfLife(board))

