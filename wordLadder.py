# morning algos
# neetcode Word Ladder


import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        patterns = collections.defaultdict(list)
        q = collections.deque([beginWord])
        visit = set([beginWord])

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        res = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for w in patterns[pattern]:
                        if w in visit:
                            continue
                        visit.add(w)
                        q.append(w)
            res += 1
        return 0


    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))