# morning algos
# neetcode search in rotated sorted array

# pseudo
# do a double binary search
# search for the value of m where m - 1 and m + 1 are both greater then m
# then reconstruct the original array which is no longer rotated
# last run another binary search for the target value
# ... this won't work because you can't run the initial search if the array isn't sorted

# new plan!
# find the index of the min
# use that to reconstruct the array
# then run a binary search for the target


# def search(nums, target):
#     #         return -1

#     shift = nums.index(min(nums))
#     reordered  = nums[shift:len(nums)] + nums[0:shift]
#     print(reordered)
#     l, r  = 0, len(nums) - 1

#     while l <= r:
#         m = (l + r) // 2

#         if reordered[m] == target:
#             # you would throw in another if statement here
#             # if m is greater than the index of target in nums then +
#             # else -
#             # but this makes no sense now that i realize it...
#             # the point is to not use index() but i already use it to find the index of the min...
#             # if we are allowed to use index then you could just run index() by itself to find
#             # whether or not the target is there in the first place

#             return m + shift
#         elif reordered[m] > target:
#             r = m - 1
#         else:
#             l = m + 1

#     return -1


# neetcode solution
def search(nums, target):
    
    l, r = 0, len(nums) - 1

    while l <= r:
        m =  (l + r) // 2

        if target == nums[m]:
            return m

        if nums[l] <= nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    
    return -1

print(search([4,5,6,7,0,1,2], 0))