#!/usr/bin/python
# Benjamin Wiens
# Cells with Odd Values in a Matrix (https://leetcode.com/problems/cells-with-odd-values-in-a-matrix)

n = 2
m = 3
indices = [[0,1],[1,1]]

class Solution:
    def oddCells(self, n: int, m: int, indices):
        row, board = [], []
        for i in range(n):
            row = [0] * m
            board.append(row)
        for index in indices:
            for i in range(m):
                board[index[0]][i] += 1
            for j in range(n):
                board[j][index[1]] += 1
        # count odds
        count = 0
        for row in board:
            for column in row:
                if column % 2 != 0:
                    count += 1
        return count

print(Solution().oddCells(n, m, indices))
