
# morning algos
# neet code Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # time: O(n)
        # space: O(n)
        differences = {}

        for i in range(len(nums)):
            if nums[i] in differences:
                return [differences[nums[i]], i]
            else:
                differences[target - nums[i]] = i
        return False

    print(twoSum([2,7,11,15], 9))