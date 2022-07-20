# morning algos
# neetcode Search a 2D Matrix

# pseudo
# first run a binary to find the row...
# then run a binary to find the actual value
# if its not there then return false but if it is return true

# my solution works and its the same as the neetcode solution
def searchMatrix(matrix, target):
    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False

    row = None
    t, b = 0, len(matrix) - 1

    while t <= b:
        m = (b + t) // 2

        if target == matrix[m][0]:
            return True
        elif target < matrix[m][0]:
            if target > matrix[m - 1][0]:
                row = m - 1
                break
            else:
                b = m - 1
        # if target > matrix[m][0]
        else:
            if m == len(matrix) - 1:
                row = m
                break
            else:
                t = m + 1
    
    l, r = 1, len(matrix[row]) - 1

    while l <= r:
        m = (l + r) // 2

        if target == matrix[row][m]:
            return True
        elif target < matrix[row][m]:
            r = m - 1
        else:
            l = m + 1

    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))