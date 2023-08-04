# morning algos
# neetcode Surrounded Regions

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        noFlip = set()

        def search(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == 'X' or (r, c) in noFlip:
                return
            if board[r][c] == 'O':
                noFlip.add((r, c))
                search(r + 1, c)
                search(r - 1, c)
                search(r, c + 1)
                search(r, c - 1)

        for r in range(ROWS):
            search(r, 0)
            search(r, COLS - 1)
        for c in range(1, COLS - 1):
            search(0, c)
            search(ROWS - 1, c)

        print(noFlip)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in noFlip:
                    board[r][c] = 'X'

        
    print(solve([
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]))