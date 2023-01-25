# morning algos
# neetcode Top K Frequent Elements

import heapq


class Solution:
    def topKFrequent(self, nums, k):
        """
        brute force solution
        frequence table hashmap, count all the instances of each num, then go through and get the k most frequent
        space O(n)
        time O(n) to generate the freq table, O(m) to go through freq table and output the k most freq -> O(m + n)
        where is the bottle neck here?
        in any instance of a solution, you will probably have to count the frequency meaning that O(n) is likely unavoidable
        -> the place to improve the algo is keeping track of the k most freq

        linear solution???
        output array which will be length k, sort nums, go through nums appending (num, freq) until you hit k length, keep track of min freq,
        if you reach a freq which is larger than the min then pop the min and append the new num
        run into a few problems
            - pop off old min but that doesn't mean that your new number's freq is the new min, it could be the largest freq
                you need to find a way to keep track of all the freq
            - using sort which O(nlogn) but I'm using sort so that we don't continuous have to continuously change and keep track of minimums
        
        maybe use a hashmap and a sorted array...

        just use a minHeap
        make frequency table, heapify, pop until length of heap is equal to k (or n largest)
        """

        # this solution works but linear solution is possible
        # time: O(n) for freq where n is the length of nums + O(m) for heapify where m is the number of distinct nums in nums + O(m) for pop to res
        # -> O(n + m) 
        # space: O(n) for freq + O(m) for heap + O(m) for res -> O(n + 2m) -> O(n + m) -> O(n + n) because n >= m -> O(2n) -> O(n)
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        heap = [(-value, key) for (key, value) in freq.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            (count, num) = heapq.pop(heap)
            res.append(num)
        
        return res

        # optimized solution
        # count = {}

        # # initialize an array where the index is mapped to frequency of the num and the value is a list of the nums with the freq
        # # of the index
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []
        # # iterate through freq array in reverse (greatest freq first), appending values to result until length of res is k
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
        
    print(topKFrequent([1], 1))
