# morning algos
# neetcode Multiply Strings

class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                res[i + j + 1] += (res[i + j] // 10)
                res[i + j] = res[i + j] % 10
        
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)


    print(multiply("2", "3"))