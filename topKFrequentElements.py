# morning algos
# top k frequent elements
# neet code 150 #5

def topKFrequent(nums, k):
    
    output = []
    num_dict = {}
    
    nums = sorted(nums)
    count = 0
    last_num = nums[0]

    # must use i in range
    # for num in nums:
    #     if num == last_num:
    #         count+=1
    #     print(nums.index(num))
    #     if num != last_num or nums.index(num) + 1 >= len(nums) - 1:
    #         num_dict[last_num] = count
    #         last_num = num
    #         count = 1

    #     if nums.index(num) == len(nums) - 1:
    #         num_dict[nums[nums.index(num)]] = 1

    x = 0
    
    while x < len(nums):
        if nums[x] == last_num:
            count += 1

        if nums[x] != last_num or x+1 > len(nums) - 1:
            num_dict[last_num] = count
            last_num = nums[x]
            count = 1
        x += 1

    
    freq_array = sorted(num_dict.values(), reverse=True)

    i = 0

    while i in range(k):
        print(i)
        if i == 0 or freq_array[i] != freq_array[i-1]:
            for num in num_dict:
                if num_dict[num] == freq_array[i]:
                    output.append(num)
        i += 1

    return output

print(topKFrequent([1,2], 2))
