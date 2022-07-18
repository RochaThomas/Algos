# morning algos
# neetcode daily temperatures

# neetcode solution... review video
# solution looks confusing but video explains it well
# go over enumerate functions
# i = index, t = temperature

def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    # stack pairs: [temp, index]
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])

    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))