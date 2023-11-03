# morning algos
# neetcode Partition Labels

class Solution:
    def partitionLabels(self, s):
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, maxRight = 0, 0
        for i, c in enumerate(s):
            size += 1
            maxRight = max(maxRight, lastIndex[c])
            if i == maxRight:
                res.append(size)
                size = 0
        return res

    print(partitionLabels("ababcbacadefegdehijhklij"))