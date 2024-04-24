# morning algos
# neet code Two Sum II

class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            tSum = numbers[l] + numbers[r]
            if tSum == target:
                return [l + 1, r + 1]
            elif tSum > target:
                r -= 1
            else:
                l += 1
            

    print(twoSum([2,7,11,15], 9))
    