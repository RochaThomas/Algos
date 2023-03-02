# morning algos
# neetcode Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):
        """
        just run a double binary search
        find the middle row
        if the target value is greater than the middle rows last value
            then cut off the first half
        if the target value is less than the middles rows first value
            then cut off the second half
        if the target value is between the first and last value of the middle
            row then run binary search on that row
        """

        # vars for top and bottom
        t, b = 0, len(matrix) - 1
        while t <= b:
            m = t + ((b - t) // 2)
            if target < matrix[m][0]:
                b = m - 1
            elif target > matrix[m][-1]:
                t = m + 1
            else:
                l, r = 0, len(matrix[m]) - 1
                while l <= r:
                    middle = l + ((r - l) // 2)
                    if target < matrix[m][middle]:
                        r = middle - 1
                    elif target > matrix[m][middle]:
                        l = middle + 1
                    else:
                        return True
                return False
        return False


    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))