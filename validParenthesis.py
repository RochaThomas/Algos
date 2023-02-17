# morning algos
# neetcode valid parenthesis

class Solution:
    def isValid(self, s):
        stack = []
        closedToOpen = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c in closedToOpen:
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


    print(isValid("()"))