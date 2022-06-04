# morning algos
# neet code 150 Arrays and Hashing #1
# there is also a one line solution using set()


# faster but more memory
# def containsDuplicate(arr):
#     map = {}
#     for num in arr:
#         if num in map:
#             return True
#         else:
#             map[num] = 1

#     return False

# slower but less memory
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False


print(containsDuplicate([1,2,3,4,5,6,6]))