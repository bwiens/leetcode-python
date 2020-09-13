class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, columns = binaryMatrix.dimensions()
        r = 0
        c = columns -1
        leftmost = -1
        while r <= rows -1 and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                leftmost = c
                c -= 1
            else:
                r += 1
        return leftmost
