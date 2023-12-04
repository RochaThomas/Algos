# morning algos
# neetcode Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = 1
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero == 0:
            for c in range(COLS):
                matrix[0][c] = 0
                
    print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))