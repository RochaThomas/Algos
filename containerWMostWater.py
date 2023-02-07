
# morning algos
# neetcode container with most water aka max area of array

class Solution:
    def maxArea(self, height):
        """
        brute force solution
        2 loops, iterate through all the heights and record the largest area you can find. area = min(h1, h2) * (i2 - i1)
        time: O(n^2)
        space: O(1)
        part to optimize: iterating through all the heights
        
        optimizing solution
        use two pointers, left and right
        take the area of iteration. area = min(h1, h2) * (r - l)
            area is dependent on 2-3 variables. h1 and h2 and the distance between the two d = (r - l)
            we know that d is continually decreasing
            area = min(h1, h2) * d => we want to maximize the minimum as we go through the array
        if min is h1 => l += 1
        elif min is h2 => r -= 1
        WHAT HAPPENS IF THEY ARE EQUAL?
            if they are equal then you look at r - 1 and l + 1 and which ever is large is the one you move
        every iterate record the max area
        return max area
        """

        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] > height[r]:
                curr_area = height[r] * (r - l)
                r -= 1
            elif height[l] < height[r]:
                curr_area = height[l] * (r - l)
                l += 1
            else:
                curr_area = height[l] * (r - l)
                while height[l] == height[r] and l < r:
                    if height[l + 1] > height[r - 1]:
                        l += 1
                    else:
                        r -= 1
            max_area = max(max_area, curr_area)
        return max_area
        
    print(maxArea([1,1]))