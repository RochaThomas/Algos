# morning algos
# neetcode valid parenthesis

class Solution:
    def isValid(self, s):
        paren = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for i in range(len(s)):
            if s[i] not in paren:
                if not stack: return False
                compare = stack.pop()
                if paren[compare] != s[i]: return False
            else:
                stack.append(s[i])
        return True if not stack else False

    print(isValid("()"))