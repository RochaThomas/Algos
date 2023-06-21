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

    def pruneWord(self, word) -> None:
        curr: TrieNode = self.root
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
        t = Trie()
        for w in words:
            t.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def search(r, c, node, word):
            if (r >= ROWS or c >= COLS or 
                r < 0 or c < 0 or
                (r, c) in visit or
                board[r][c] not in node.children):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
                node.isWord = False
                t.pruneWord(word)
            search(r + 1, c, node, word)
            search(r - 1, c, node, word)
            search(r, c + 1, node, word)
            search(r, c - 1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                search(r, c, t.root, "")

        return list(res)


    print(findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))