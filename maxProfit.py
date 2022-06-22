# morning algos
# neetcode best time to buy and sell stock aka max profit

# this solution works
# def maxProfit(prices):
#     max = 0
#     low = prices[0]

#     for i in range(len(prices)):
#         if prices[i] < low:
#             low = prices[i]
#         else:
#             dif = prices[i] - low
#             if dif > max:
#                 max = dif
            
#     return max

# solution using pointers but first solution is better
def maxProfit(prices):
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    
    return maxP



print(maxProfit([7,1,5,3,6,4]))