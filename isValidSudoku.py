

# morning algos
# neet code ValidSudoku

# first check across the row --->
# any repeating nums?
# next check down the column

# last check 3 by 3
# this is where efficiency could get muddy
# remember at this point you have already "checked" 5 of the 9 squares in the 3x3
# only 4 squares need to be checked but this varies based on position

# the above notes should be re ordered

def isValidSudoku(board):

    # first i'm checking the 3 by 3
    num_dict = {}

    x_mult = 0
    y_mult = 0

    while y_mult < 3:
        for x in range(3 * x_mult, 3 * (x_mult + 1)):
            for y in range(3 * y_mult, 3 * (y_mult + 1)):
                if board[x][y] != "." and board[x][y] not in num_dict:
                    num_dict[board[x][y]] = 1
                elif board[x][y] in num_dict:
                    return False
        
        x_mult += 1
        num_dict = {}

        if x_mult > 2:
            y_mult += 1
            x_mult = 0

    # now check across
    for y in range(9):
        for num in board[y]:
            if num != "." and num not in num_dict:
                num_dict[num] = 1
            elif num in num_dict:
                return False
        num_dict = {}

    # last check down
    for x in range(9):
        for y in range(9):
            if board[y][x] != "." and board[y][x] not in num_dict:
                num_dict[board[y][x]] = 1
            elif board[y][x] in num_dict:
                print("x",x)
                print("y",y)
                print(board[y][x])
                return False
        num_dict = {}

    return True



print(isValidSudoku([
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]))
