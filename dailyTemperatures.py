# morning algos
# neetcode daily temperatures

class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                val, idx = stack.pop()
                res[idx] = i - idx
            stack.append([temperatures[i], i])
        return res


    print(dailyTemperatures([73,74,75,71,69,72,76,73]))