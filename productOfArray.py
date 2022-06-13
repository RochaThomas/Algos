
# def productExceptSelf(nums):

#     # works but is too slow and too much mem...
#     output = []
#     original_length = len(nums)

#     nums += nums

#     for i in range(original_length):
#         prod = 1
#         for x in range(i + 1, original_length + i):
#             prod *= nums[x]
#         output.append(prod)

#     return output

# most optimal solution
def productExceptSelf(nums):
    output = [1] * len(nums)
    
    prefix = 1

    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]

    print(output)
    postfix = 1

    for i in range(len(nums) - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]

    return output

print(productExceptSelf([1,2,3,4]))