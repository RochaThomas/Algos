

# morning algos
# neet code Valid Sudoku


import collections


class Solution:
    def isValidSudoku(board):
        """
        brute force solution
        loop through all rows and all numbers in row making sure there aren't repeats
        repeat for columns
        repeat for 3x3 box
        time: 3n^2 -> O(n^2)
        space: O(n) where n is the length of a row or column... 9
        place to improve effeciency: in the brute force solution you are revisiting the same
        indexes over and over again

        optimizing solution
        iterate through the enitre sudoku board recording the row and column of every number
        if there is a number that has two instances with the same row or column then return false
        if there are two of the same numbers within the same 3x3 matrix then return false
        tough part is keeping track of the indices when checking the box
        """

        ROWS, COLS = 9, 9
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        # record all the indexes of all the instance of a number by number making sure there are no repeats in cols or rows
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[((r//3, c//3))]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[((r//3, c//3))].add(board[r][c])
                
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
