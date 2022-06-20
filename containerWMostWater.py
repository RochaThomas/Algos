
# morning algos
# neetcode container with most water aka max area of array

def maxArea(height):
    f, l, most = 0, len(height) - 1, 0

    while l - f >= 1:
        area = 0
        if height[f] <= height[l]:
            area = (l-f) * height[f]
            f += 1
        else:
            area = (l-f) * height[l]
            l -= 1
        
        if area > most:
            most = area

    return most

print(maxArea([1,1]))