# morning algos
# neet code Contains Duplicate


class Solution:
    def containsDuplicate(self, nums):
        # faster solution that sacrifices a little bit of space
        # Time: O(n)
        # Space: O(n)
        n = set()

        for num in nums:
            if num in n: return True
            n.add(num)
        return False

        # slower solution but doesn't sacrafice space
        # Time: O(nlogn) because of sorting
        # Space: O(1)
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False



    print(containsDuplicate([1,2,3,1]))