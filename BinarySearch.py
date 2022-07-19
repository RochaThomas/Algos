# morning algos
# neet code binary search

def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m  = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

    return  -1

print(search([5], 5))