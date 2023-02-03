
# morning algos
# neet code valid palindrome

class Solution:
    def isPalindrome(self, s):
        """
        go through the string from beginning to middle
        check if the char you are reading at the start is the same as the one you are reading from the end
        incrementally move closer to the middle
        have to deal with cases where the char is non-alphanumeric or if the strings differ in cases

        dealing with cases and non-alph characters can be handled two ways
        before comparing run a loop that forces all to the same case and removes non-alph chars, then run comparison loop
        in the comparison loop, remove or skip non-alph chars and force chars to same case, then compare after
        """

        l, r = 0, len(s) - 1
        while l < r:
            # check if non-alph
            skip = False
            if self.alphaNumHelper(s[l]) == False:
                l += 1
                skip = True
            if self.alphaNumHelper(s[r]) == False:
                r -= 1
                skip = True
            if skip == True: continue
            
            # force same case and compare
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    # if interviewer doesn't want you to use built in isalnum() function then implement your own
    # otherwise just use isalnum() its faster
    def alphaNumHelper(self, c):
        if ((ord(c) >= ord('A') and ord(c) <= ord('Z')) or
            (ord(c) >= ord('a') and ord(c) <= ord('z')) or
            (ord(c) >= ord('0') and ord(c) <= ord('9'))):
            return True
        return False

    print(isPalindrome("0P"))