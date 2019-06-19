#!/usr/bin/python 
# Benjamin Wiens
# Lonely Pixel I (https://leetcode.com/problems/lonely-pixel-i/)
# Leetcode Accepted

picture = [['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

class Solution:
    def findLonelyPixel(self, picture):
        hmap_rows, hmap_columns = {}, {}
        result = 0
        row_length = len(picture)
        column_length = len(picture[0])
        for rindex, row in enumerate(picture):
            for cindex, column in enumerate(row):
                if column == 'B':
                    if rindex not in hmap_rows:
                        hmap_rows[rindex] = 1
                    else:
                        hmap_rows[rindex] += 1
                    if cindex not in hmap_columns:
                        hmap_columns[cindex] = 1
                    else:
                        hmap_columns[cindex] += 1
        for rindex, row in enumerate(picture):
            for cindex, column in enumerate(row):
                if column == 'B':
                    if hmap_rows.get(rindex) == 1:
                        if hmap_columns.get(cindex) == 1:
                            result += 1
        return result

print(Solution().findLonelyPixel(picture))
