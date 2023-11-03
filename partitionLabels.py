# morning algos
# neetcode Partition Labels

class Solution:
    def partitionLabels(self, s):
        letter = {}
        for i, v in enumerate(s):
            letter[v] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, letter[c])
            if i == end:
                res.append(size)
                size = 0
        return res



    print(partitionLabels("ababcbacadefegdehijhklij"))