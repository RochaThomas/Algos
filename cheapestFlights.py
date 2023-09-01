# morning algos
# neetcode Cheapest Flights with K Stops

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            prices = temp


        return prices[dst] if prices[dst] != float('inf') else -1









    (findCheapestPrice( 4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
