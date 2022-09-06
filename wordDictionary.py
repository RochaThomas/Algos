# morning algos
# neetcode Design Add and Search Words Data Structure

# neetcode solution but its too slow to pass the test
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.endOfWord = False

# class WordDictionary:
#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
#         curr = self.root

#         for c in word:
#             if c not in curr.children:
#                 curr.children[c] = TrieNode()
#             curr = curr.children[c]
#         curr.endOfWord = True

#     def search(self, word: str) -> bool:
#         def dfs(j, root):
#             curr = root

#             for i in range(j ,len(word)):
#                 c = word[i]
#                 if c == '.':
#                     for child in curr.children.values():
#                         if dfs(i + 1, child):
#                             return True
#                     return False
#                 else:
#                     if c not in curr.children:
#                         return False
#                     curr = curr.children[c]
#             return curr.endOfWord

#         return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# working solution for leetcode

from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.d = defaultdict(list)

    def addWord(self, word):
        self.d[len(word)].append(word)

    def search(self, word):
        words = self.d[len(word)]

        for each in words:
            if each == word: return True

            for e, w in zip(each, word):
                if w == '.': continue
                if e != w: break
            else: return True
        return False