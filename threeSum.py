# morning algos
# neetcode three Sum

def threeSum(nums):
    output = []
    nums.sort()

    for i, a in enumerate(nums):
        if  i > 0 and a == nums[i-1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                output.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return output

print(threeSum([-1,0,1,2,-1,-4]))