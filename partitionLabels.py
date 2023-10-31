# morning algos
# neetcode Partition Labels

class Solution:
    def partitionLabels(self, s):
        letterIndex  = {}
        res = []

        for i, v in enumerate(s):
            letterIndex[v] = i

        end = 0
        size = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, letterIndex[c])
            if i == end:
                res.append(size)
                size = 0
        return res

    print(partitionLabels("ababcbacadefegdehijhklij"))