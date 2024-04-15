

# morning algos
# neetcode Group Anagrams

import collections


class Solution:
    def groupAnagrams(strs):
        # anagramDict = {}
        # for s in strs:
        #     k = ",".join(sorted(s))
        #     if k in anagramDict:
        #         anagramDict[k].append(s)
        #     else:
        #         anagramDict[k] = [s]
        # return anagramDict.values()

        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        print(res)

        return res.values()

        

    print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))