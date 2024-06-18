# interview prep practice
# Fibonacci Sequence
def fibSeq(n):
    res = [0, 1]
    prev, curr = res[0], res[1]
    for i in range(n):
        temp = prev + curr
        res.append(temp)
        prev = curr
        curr = temp
    return res
    
def recFibSeq(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return recFibSeq(n - 2) + recFibSeq(n - 1)
    
def recFibSeqCaching(n):
    cache = {}
    def helper(n):
        if n in cache:
            return cache[n]
        elif n == 1:
            value = 1
        elif n == 0:
            value = 0
        else:
            value = helper(n - 1) + helper(n - 2)
        
        cache[n] = value
        return value
    
    res = []
    for i in range(n + 1):
        res.append(helper(i))
            
    helper(10)
    return res

print(recFibSeqCaching(n=10))