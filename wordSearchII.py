# morning algos
# neetcode Word Search 2

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def pruneWord(self, word):
        curr = self.root
        keyMap = []
        for letter in word:
            keyMap.append((curr, letter))
            curr = curr.children[letter]

        for parent, childKey in reversed(keyMap):
            child = parent.children[childKey]
            if len(child.children) == 0:
                del parent.children[childKey]
            else:
                return

class Solution:
    def findWords(self, board, words):
        t = Trie()
        for w in words:
            t.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def search(r, c, node, word):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or
                (r,c) in visited or board[r][c] not in node.children):
                return
            
            word += board[r][c]
            node = node.children[board[r][c]]
            visited.add((r,c))
            if node.end:
                res.add(word)
                node.end = False
                t.pruneWord(word)
            
            search(r + 1, c, node, word)
            search(r - 1, c, node, word)
            search(r, c + 1, node, word)
            search(r, c - 1, node, word)

            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                search(r, c, t.root, "")
        
        return list(res)

    print(findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))