# morning algos
# neetcode Distinct Sequences

class Solution:
    def numDistinct(self, s, t):
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
                return cache[(i, j)]
            else:
                cache[(i, j)] = dfs(i + 1, j)
                return cache[(i, j)]
        return dfs(0, 0)

    print(numDistinct("rabbbit", "rabbit"))