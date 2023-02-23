# morning algos
# neetcode generate parenthesis

class Solution:
    def generateParenthesis(self, n):
        stack = []
        res = []
        def backtrack(openN, closedN):
            # base case when the stack has the correct order and number of parenthesis
            # make the stack into a string and append to result
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # only add open paren when number of open is less than n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # pop because we are only using 1 stack so we pop off the paren we just added
                # so that we can make more combinations of parenthesis
                stack.pop()
            
            # only add close paren when num of closed is less than open
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res


    print(generateParenthesis(3))