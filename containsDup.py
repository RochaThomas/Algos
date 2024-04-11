# morning algos
# neet code Contains Duplicate


class Solution:
    def containsDuplicate(self, nums):
        count = {}
        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1
        return False

    print(containsDuplicate([1,2,3,1]))