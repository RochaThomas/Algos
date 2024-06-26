# morning algos
# neetcode largest rectangle in histogram


class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
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
