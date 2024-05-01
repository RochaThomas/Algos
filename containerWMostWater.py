
# morning algos
# neetcode container with most water aka max area of array

class Solution:
    def maxArea(self, height):
        # READ ME
        # the else case here is important and confusing
        # the else case contains both height[l] < height[r] and height[l] == height[r]
        # you can run the same l += 1 case because whatever is shifted is arbitrary
        # the area bounded by the height[l] or height[r] has already been maximized
        # even if height[l + 1] or height[r - 1] is higher, the next calculation of the area
        # involving height[l] or height[r] won't be any larger because (r - l) will be smaller
        # as r and l are shifted and the min height will stay the same at height[l] or height[r]
        
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = min(height[l], height[r])
            res = max(res, (r - l) * area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res

        
    print(maxArea([1,1]))