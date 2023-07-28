# morning algos
# neetcode palindrome partitioning

class Solution:
    def partition(self, s):
        res = []
        curr = []

        def backtrack(i):
            if i >= len(s):
                res.append(curr[:])
                return res
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    curr.append(s[i: j + 1])
                    backtrack(j + 1)
                    curr.pop()
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        backtrack(0)
        return res

    print(partition("aab"))