# morning algos
# neetcode Rotate Image

class Solution:
    def rotate(self, matrix):
        
        l, r  = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save top left
                topLeft = matrix[top][l + i]

                # save bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1

    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))