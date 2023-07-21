# morning algos
# neetcode word search

class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def search(r, c, i):
            if i >= len(word):
                return True
            if  (r >= ROWS or c >= COLS or r < 0 or c < 0 or board[r][c] != word[i] or (r,c) in visited):
                return False
            
            visited.add((r,c))
            res = (
                search(r + 1, c, i + 1) or 
                search(r - 1, c, i + 1) or 
                search(r, c + 1, i + 1) or 
                search(r, c - 1, i + 1))
            visited.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if search(r, c, 0): return True
        return False

    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))