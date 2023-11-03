# morning algos
# neetcode Merge Triplets to Form Target Triplet

class Solution:
    def mergeTriplets(self, triplets, target):
        good = set()

        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            for i, v in enumerate(trip):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3



    print(mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))