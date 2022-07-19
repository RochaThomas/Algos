# morning algos
# neetcode largest rectangle in histogram


# neetcode solution
# rewatch video
# focus on how the function is running the areas in parallel

def largestRectangleArea(heights):
    maxArea = 0

    # pair of elements : [index, height]
    stack = []

    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))
    
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    
    return maxArea
print(largestRectangleArea([2,1,5,6,2,3]))