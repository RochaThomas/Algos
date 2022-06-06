
# morning algos
# neet code #3
# two sum

# first try
# def twoSum(nums, target):
#     output = []
#     for i in range(len(nums)):
#         if nums[i] <= target:
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     output.append(i)
#                     output.append(j)
#                     return output
    
#     return False

# second try is a little faster
# def twoSum(nums, target):
#     output = []

#     for i in range(len(nums)):
#         find_num = target - nums[i]
#         if find_num == nums[i]:
#             temp = nums.copy()
#             temp.remove(nums[i])
#             if find_num in temp:
#                 output.append(i)
#                 output.append(temp.index(find_num) + 1)
#                 return output
#         else:
#             if find_num in nums:
#                 output.append(i)
#                 output.append(nums.index(find_num))
#                 return output
#     return False


# optimized solution
# faster but not perfect
def twoSum(nums, target):
    num_dict = {}

    for i in range(len(nums)):
        find_num = target - nums[i]
        if find_num not in num_dict:
            num_dict[nums[i]] = i
        else:
            return [num_dict[find_num], i]
    return False

print(twoSum([0,1,2,3,4,5,9], 14))