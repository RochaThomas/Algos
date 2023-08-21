# morning algos
# neetcode Surrounded Regions

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])
        noFlip = set()

        def trail(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in noFlip or board[r][c] != 'O':
                return
            noFlip.add((r, c))
            trail(r + 1, c)
            trail(r - 1, c)
            trail(r, c + 1)
            trail(r, c - 1)
                

        for r in range(ROWS):
            trail(r, 0)
            trail(r, len(board[0]) - 1)

        for c in range(COLS):
            trail(0, c)
            trail(len(board) - 1, c)

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