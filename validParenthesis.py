# morning algos
# neetcode valid parenthesis

class Solution:
    def isValid(self, s):
        stack = []
        closedToOpen = {')':'(', ']':'[', '}':'{'}

        if len(s) % 2 != 0 or s[0] in closedToOpen.keys() or s[-1] in closedToOpen.values(): return False
        
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