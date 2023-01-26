
# morning algos
# neetcode Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums):
        """
        brute force solution
        2 loops, 1 nested in the other, first goes through nums, second goes through the other nums and skips nums[i]
        append product to a result array
        time: O(n^2)
        space: O(n)

        must be O(n), linear time complexity indicates algo should have 1 loop maybe...
        use prefix and postfix of every position and multiple them together to get the correct output
        do one loop to get the prefixes and store them in the output[i] where i corresponds to nums[i]
        then do another loop in reverse to get the post fixes and multiply them with the output that is storing
        the prefixes
        time: O(2n) => O(n)
        space: O(1)
        """

        #have a holder var to store the current pre or post fix value
        res = [1] * len(nums)
        holder = 1
        # setting prefixes
        for i in range(len(nums)):
            res[i] = holder
            holder *= nums[i]
        
        # reset holder
        holder = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= holder
            holder *= nums[i]
        return res