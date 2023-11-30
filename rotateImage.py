# morning algos
# neetcode Rotate Image

class Solution:
    def rotate(self, matrix):
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t, b = l, r
                topLeft = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = topLeft
            l += 1
            r -= 1


    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))