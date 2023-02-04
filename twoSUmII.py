# morning algos
# neet code Two Sum II

class Solution:
    def twoSum(self, numbers, target):
        """
        normally
        use a hashmap and iterate through nums, store the difference between nums and target as the key and index of num as the value
        check if num is in the hashmap on every iteration and return value of num and index of num
        but this problem must be done in constant space... no hashmaps...

        brute force is to use two for loops (nested)
        iterate through nums, for every num iterate through nums looking for a counter part that adds to target
        time: O(n^2)

        use two pointers
        if the sum of the two nums is greater than target r -= 1
        if the sum of the two nums is less than the target l += 1
        why does this work
            its in sorted order so if nums[l] + nums[r] is too big the only way to get it smaller is to decrement r
            change l won't work because you already checked nums[l - 1] and nums[l + 1] is just going to increase the sum
            because its in sorted order nums[l - 1] + nums[r] < nums[l] + nums[r + n]
        time: O(n)
        space: O(1)
        """

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return False

    print(twoSum([2,7,11,15], 9))
    