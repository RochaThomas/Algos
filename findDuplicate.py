# morning algos
# neetcode find the duplicate

class Solution:
    def findDuplicate(self, nums):
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


    print(findDuplicate([1,3,4,2,2]))