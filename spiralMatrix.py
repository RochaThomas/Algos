# morning algos
# neetcode Spiral Matrix

class Solution:
    def spiralOrder(self, matrix):
        res = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)

        while l < r and t < b:
            # get every i in top row
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            # get every i in right col
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and t < b):
                break

            # get every i in bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            # get every i in left col
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res

    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))