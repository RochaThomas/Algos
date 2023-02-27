# morning algos
# neetcode car fleet

class Solution:
    def carFleet(self, target, position, speed):
        """
        each car can be graphed as a linear equation
        y = mx + b
        where m is the speed of the car and b (the y intercept) is th starting position of the car
        when the line for one car intersects with another car. the two cars form a fleet and travel at the slope
        of the slower car

        my solution would be to iterate throught the cars, speeds, positions
        if one car intersects with another before the target value, group them together in an array that maps to a tuple
        of (speed, position) of the slowest car
        else create a new hashmap entry
        at the end return the length of the hashmap keys

        FOR THIS NEETCODE SOLUTION
        THE IDEA IS RELATIVELY THE SAME I JUST DIDN'T KNOW HOW TO COME UP WITH THE SOLUTION USING STACKS
        MY SOLUTION MAY HAVE WORKED BUT WOULD LIKELY BE MORE ROBUST, I DON'T KNOW HOW THE TIME COMPLEXITIES WOULD
        HAVE COMPARED
        """
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []

        # iterate through in reverse sorted order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


    print(carFleet(10, [6,8], [3,2]))