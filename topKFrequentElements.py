# morning algos
# top k frequent elements
# neet code 150 #5

def topKFrequent(nums, k):
    
    output = []
    num_dict = {}
    
    nums = sorted(nums)
    count = 0
    last_num = nums[0]

    x = 0
    
    while x < len(nums):
        if nums[x] == last_num:
            count += 1
        else:
            num_dict[last_num] = count
            last_num = nums[x]
            count = 1

        if x+1 >= len(nums):
            num_dict[last_num] = count
        x += 1

    
    freq_array = sorted(num_dict.values(), reverse=True)

    i = 0
    x = 0

    while i < len(freq_array) and x <= k:
        if i == 0:
            for num in num_dict:
                if num_dict[num] == freq_array[i]:
                    output.append(num)
                    x += 1
        elif freq_array[i] != freq_array[i-1]:
            for num in num_dict:
                if num_dict[num] == freq_array[i]:
                    output.append(num)
                    x += 1
        i += 1

    return output

print(topKFrequent([1], 1))
