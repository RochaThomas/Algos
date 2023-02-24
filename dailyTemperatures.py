# morning algos
# neetcode daily temperatures

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        brute force
        2 loops
        iterate through temps and then rest of temps, recording the difference in index between lower temp and higher temp
        problem is you are repeating a lot of work, searching through the same values you already know over and over

        optimization
        use two stacks pop from one to the other
        creating a monotonic decreasing order
        """

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res

    print(dailyTemperatures([73,74,75,71,69,72,76,73]))