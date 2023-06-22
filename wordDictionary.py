# morning algos
# neetcode Design Add and Search Words Data Structure

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            for i in range(j, len(word)):
                letter = word[i]
                if letter == '.':
                    for child in node.children.values():
                        if dfs(child, i + 1): return True
                if letter not in node.children:
                    return False
                node = node.children[letter]
            return node.end
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
