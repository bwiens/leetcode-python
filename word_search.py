#!/usr/bin/python
# Benjamin Wiens
# Word Search (https://leetcode.com/problems/word-search)

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"
class Solution:
    def exist(self, board, word):
        visited = {}
        def dfs(rid, cid, word, visited, found):
            if len(word) == 0:
                return True
            if rid < 0 or cid < 0 or rid >= len(board) or cid >= len(board[0]) or (rid, cid) in visited or board[rid][cid] != word[0]:
                return False
            visited[(rid, cid)] = 1
            res = dfs(rid+1, cid, word[1:], visited, found) or dfs(rid, cid+1, word[1:], visited, found) or dfs(rid-1, cid, word[1:], visited, found) or dfs(rid, cid-1, word[1:], visited, found)
            #print(visited, word, res)
            del visited[(rid, cid)]
            return res
            
            
            
        #for every place in the grid, check if word exists
        for rid, row in enumerate(board):
            for cid, column in enumerate(row):
                if column == word[0]:
                    visited = {}
                    found = 0
                    if dfs(rid, cid, word, visited, found):
                        return True
        return False

print(Solution().exist(board, word))
