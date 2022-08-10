# morning algos
# neetcode find the duplicate

# tricky problem, pretty much just memorization for this one
def findDuplicate(nums):
    s, f = 0, 0

    while True:
        s = nums[s]
        f = nums[nums[f]]

        if s == f:
            break

    s2 = 0
    while True:
        s = nums[s]
        s2 = nums[s2]

        if s == s2:
            return s

print(findDuplicate([1,3,4,2,2]))