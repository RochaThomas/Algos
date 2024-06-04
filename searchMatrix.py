# morning algos
# neetcode Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):
        t, b = 0, (len(matrix) - 1)
        while t <= b:
            rowIdx = (t + b) // 2
            if target > matrix[rowIdx][-1]:
                t = rowIdx + 1
            elif target < matrix[rowIdx][0]:
                b = rowIdx - 1
            else:
                l, r = 0, (len(matrix[rowIdx]) - 1)
                while l <= r:
                    m = (l + r) // 2
                    if matrix[rowIdx][m] < target:
                        l = m + 1
                    elif matrix[rowIdx][m] > target:
                        r = m - 1
                    else:
                        return True
                return False
        return False



    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))