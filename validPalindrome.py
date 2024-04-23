
# morning algos
# neet code valid palindrome

class Solution:
    def isPalindrome(self, s):
        # solution 1
        # take string and convert into lowercase no space
        # def convertString(toConvert):
        #     converted = ""
        #     for c in s:
        #         if c.isalnum():
        #             converted += c.lower()
        #     return converted
        
        # converted = convertString(s)
        # l, r = 0, len(converted) - 1
        # while l < r:
        #     if converted[l] != converted[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True
    
        # solution 2
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True

    print(isPalindrome("0P"))