

# morning algos
# neetcode longest repeating character replacement

class Solution:
    def characterReplacement(self, s, k):
        """
        brute force solution
        two loops, one iterates through the chars in s and for every char in s you have another loop iterating through the rest
        of the chars
            count how many times you see a letter that isn't the one you want to repeat
            when you hit k times, compare to the longest and go to the next letter
        time: O(n^2)

        optimized solution
        two pointers... sliding window
        hard part of this problem is keeping track of the most frequent letter used in a given substring of the s

        left and right pointers
        iterate right counting the occurences of the chars
        given the most frequent char in the substring s[l:r + 1], iterate r until you have hit a char that isn't
        the most frequent k times
        then compare current substring length to longest
        iterate l

        maybe use a max heap to keep track of the most frequent letter...?
        """
        # hashmap to count occurences of char in substring
        count = {}
        # pointers to establish window
        l, r = 0, 0
        # var to keep track of longest substring with replacement
        longest = 0

        maxf = 0

        # while loop to iterate the entire string
        while r < len(s):
            # counting occurences of a char and storing it in hashmap
            # incrementing if its already there and setting if it isnt
            count[s[r]] =  1 + count.get(s[r], 0)
            # maxf keeps track of the highest frequency of a char in the substring
            # we only update this if the maxf changes... meaning that the new char of s[r] updated its freq in the count
            # hashmap and is now greater than the current maxf
            # we only need to keep track of maxf because the result will only be changed if you find a larger frequency
            # smaller frequencies will have no effect on the outcome so their is no need to keep track of that
            maxf = max(maxf, count[s[r]])

            # increment l and update count hashmap accordingly, decrementing the count for the letter that is no longer
            # in the window
            # again... we use maxf in place of searching through the entire count hashmap to find the highest frequency
            # of the current substring
            # this is because it decreases having to search through 26 possible values every iteration and
            # there would be no need to update the result of longest unless the max frequency of any char in the current window
            # was larger than the max f of any char of previous windows
            # if this confuses you go watch neetcode's video he explains it very well
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # compare longest to the current window
            longest = max(longest, r - l + 1)
            r += 1

        return longest



    print(characterReplacement("AABABBA", 1))