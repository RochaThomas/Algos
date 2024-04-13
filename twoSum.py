
# morning algos
# neet code Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = {}
        for i in range(len(nums)):
            if target - nums[i] in n:
                return [i, n[target - nums[i]]]
            n[nums[i]] = i
        return False

    print(twoSum([2,7,11,15], 9))