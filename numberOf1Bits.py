# morning algos
# neetcode Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res

        # res = 0
        # while n:
        #     res += n % 2
        #     n = n >> 1
        # return res

    # print(hammingWeight(n = 00000000000000000000000010000000))