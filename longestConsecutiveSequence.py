# morning algos
# neetcode longest consecutive sequence

# needed help to figure this solution out
def longestConsecutive(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums:
        if (num - 1) not in nums_set:
            length = 0
            while (num + length) in nums_set:
                length += 1
            if length > longest:
                longest = length
    return longest



print(longestConsecutive([100,4,200,1,3,2]))
