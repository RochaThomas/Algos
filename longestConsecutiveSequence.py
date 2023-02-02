# morning algos
# neetcode longest consecutive sequence

class Solution:
    def longestConsecutive(self, nums):
        """
        brute force
        put it all in a hashmap iterate through keys checking if the next number is in the map and incrementing length
        you could also sort then iterate through but this would make it O(n log n) and the solution needs to be O(n)

        what you need to figure out is how to find the beginning of a sequence...NO LEFT NEIGHBOR is the key to the solution
        array -> set (gives you instant time access to keys (nums in this case))
        iterate through set, if num doesnt have a left number see how long the sequence goes, when it ends, iterate again, record max
        time: O(n) to iterate through set and O(n) to go through sequence for each starting num -> O(2n) -> O(n)
        space: O(n) for the set
        """
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0

        nums = set(nums)
        length, longest = 1, 1

        for n in nums:
            if n - 1 in nums:
                continue
            else:
                m = n
                while m + 1 in nums:
                    m += 1
                    length += 1
                longest = max(longest, length)
                length = 1
        return longest





    print(longestConsecutive([100,4,200,1,3,2]))
