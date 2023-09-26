# morning algos
# neetcode Climb Stairs

class Solution:
    def climbStairs(self, n):
        one, two = 1, 1
        for i in range(n):
            temp = two
            two += one
            one = temp
        return one


    print(climbStairs(2))