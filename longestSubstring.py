
# morning algos
# neet code longest substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        brute force solution
        iterate through string
            for every iteration have a loop that goes through the rest of the string until it reaches a
            repeating character or the end of the string
                compare the length of that substring to the length of the longest substring and update accordingly
        time: O(n^2) because of nested loops
        space: O(1)

        optimized solution
        sliding window using two pointers, left and right
        iterate r, while r is less than the length of the string
        start at l creating a 'substring' from l to r, record each character in a set
        if r is in the set then compare from l to r with longest substring
        increment l and remove char of l from set until you reach the char that r is repeating
        return longest at the end
        """
        l, r = 0, 1
        characters = set()
        characters.add(s[l])
        longest = 1

        while r < len(s):
            if s[r] in characters:
                longest = max(longest, r - l)
                while s[l] != s[r]:
                    characters.remove(s[l])
                    l += 1
                l += 1
            else:
                characters.add(s[r])
            r += 1
        return longest

        # more concise version but same thing
        # l, r = 0, 0
        # characters = set()
        # longest = 0

        # while r < len(s):
        #     while s[r] in characters:
        #         characters.remove(s[l])
        #         l += 1
        #     characters.add(s[r])
        #     r += 1
        #     longest = max(longest, r - l)
        # return longest


    print(lengthOfLongestSubstring("abcabcbb"))