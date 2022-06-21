
# morning algos
# neetcode trapping rain water

# first try this solution won't work
# def trap(height):
#     total = 0
#     start = 0
#     for i in range(len(height) - 1):
#         if height[i] > height[i + 1]:
#             start = i
#             break
    
#     runner = start + 2
#     # print(start)

#     while runner < len(height):
#         if height[runner] < height[start]:
#             runner += 1
#             continue
#         else:
#             area = (runner - start - 1) * height[start]
#             for x in range(runner - 1, start, -1):
#                 area -= height[x]
#             # print(area)
#             total += area
            
#             for i in range(runner, len(height) - 1):
#                 if height[i] > height[i + 1]:
#                     start = i
#                     break
#             print(start)
#             runner = start + 2

        

#     return total

# second try neetcode solution using two pointers
# time complexity O(1)
def trap(height):
    if not height: return 0

    l, r  = 0, len(height) - 1

    l_max = height[l]
    r_max = height[r]

    total = 0

    while r > l:
        if l_max < r_max:
            l += 1
            l_max = max(l_max, height[l])
            total += l_max - height[l]
        else:
            r -= 1
            r_max = max(r_max, height[r])
            total += r_max - height[r]

    return total

print("rain trapped", trap([0,1,0,2,1,0,1,3,2,1, 2, 1]))
#                           0 1 2 3 4 5 6 7 8 9 10 11
