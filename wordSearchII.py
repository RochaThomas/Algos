# morning algos
# neetcode Word Search 2

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def pruneWord(self, word) -> None:
        curr: TrieNode = self
        nodeAndChildKey: list[tuple[TrieNode, str]] = []
        for char in word:
            nodeAndChildKey.append((curr, char))
            curr = curr.children[char]

        for parentNode, childKey in reversed(nodeAndChildKey):
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0:
                del parentNode.children[childKey]
            else:
                return

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 
                or c < 0 
                or r == ROWS 
                or c == COLS 
                or (r,c) in visit 
                or board[r][c] not in node.children):
                return 
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                node.isWord = False
                root.pruneWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
            
        return list(res)

    print(findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))