# morning algos
# neetcode word search

class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or board[r][c] == "."):
                return False
            
            temp = board[r][c]
            board[r][c] = "."
            res = (
                dfs(r + 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or 
                dfs(r - 1, c, i + 1) or 
                dfs(r, c -1, i + 1)
                )

            board[r][c] = temp
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False



    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))