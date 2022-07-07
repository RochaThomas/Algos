
# morning algos
# neetcode sliding window maximum

# first try invalid solution look at line 29
# def maxSlidingWindow(nums, k):
#     output = []
#     window = []
#     highest = -float('inf')
#     second_highest = -float('inf')

#     l = 0

#     for r in range(len(nums)):

#         window.append(nums[r])

#         if nums[r] > highest:
#             second_highest = highest
#             highest = nums[r]
#         elif nums[r] >= second_highest:
#             second_highest = nums[r]

#         if len(window) == k:
#             output.append(highest)
#             window.remove(nums[l])
#             if nums[l] == highest:
#                 highest = second_highest
#                 # this next line is where this solution hangs...
#                 second_highest = nums[r]
#             l += 1

#     return output
    
    # pseudo coding

    # first propagate the window
    # use logic to set highest and second highest
    #   this same logic will be used for the rest so structure accordingly
    # shift window
    #   for every shift push highest to output

    # iterate through
    # set highest
    # if highest gets replaced
    # make old highest to second highest
    # if not greater than highest, check against second highest
    # when sliding the window, if what gets popped is highest then second highest become highest
    # check highest as <= need the equal to sign

#  the real solution requires the use of a data structure called a queue, in this case a deque

import collections


def maxSlidingWindow(nums, k):
    output = []
    q = collections.deque()
    l, r = 0, 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output


print(maxSlidingWindow([1,-1], 1))