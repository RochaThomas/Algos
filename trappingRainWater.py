
# morning algos
# neetcode trapping rain water

class Solution:
    def trap(self, height):
        """
        no obvious brute force solution

        iterate through with two pointers
            left will hit first local max and right will stop when its >= left
                wont necessarily work because what if the fist left is the highest point, then right won't stop

        left at start and right at end
            total += (r - l) * min(l, r), record min move min side
            total -= min(height[l], height[r])

        ...i'm stumped
        things i learned => boil the problem down to the smallest problem first then work your way bigger
            smallest problem here is how to tell how much water can be stored at one spot/ one index of height
            the equation for this would be the min(maxLeftHeight, maxRightHeight) - height[i]
        know this equation we can iterate through 1 time forwards to get all maxLefts for each index
            then once in reverse to get all maxRights for each index
            then a last time to get the total water for each spot summed up
            this requires O(n) time and O(n) space
        but you can also do this with constant memory and linear time
            how!? well, we know that all we need is the min of maxHeight of left and right pointers
                so... for any given point if you are keeping track of maxLeft and maxRight and updating them on every iteration
                    you will know the min you need by comparing the max left and max right
        """
        if not height: return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
                
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        
        return res

    print("rain trapped", trap([0,1,0,2,1,0,1,3,2,1, 2, 1]))
#                           0 1 2 3 4 5 6 7 8 9 10 11
