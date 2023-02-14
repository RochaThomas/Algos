
# morning algos
# neetcode permutation in string, check inclusion

def checkInclusion(s1, s2):
    """
    brute force
    make a count hashmap of chars in s1
    iterate through s2 for every iteration of s2 iterate through the remaining length of s2 such that substring of s2 is equal
    to length of s1 counting occurances of characters
    if counts of hashmaps for s1 and substring of s2 are the same return true
    if true never returns then return false

    optimized solution
    l and r pointers establishing a window. window length should never be longer than the length of s1
    make a hashmap to count s1 chars
    iterate r
    if s2[r] not in s1 count then increment l
        when l increments add back in s[l] if s[l] is in s1 count
    """
    if len(s1) > len(s2): return False

    s1Count, s2Count = [0] * 26, [0] * 26

    # initialize s1Count and s2Count for first window
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    # matches at the end will equal 26 if the count for all chars in the alphabet are equal
    matches = 0
    # initialize number of matches for first window
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        
        l += 1

    return matches == 26


    # my solution works but its slow with bad memory
    # l, r = 0, 0
    # count = {}

    # for c in s1:
    #     count[c] = 1 + count.get(c, 0)

    # while r < len(s2):
    #     if r - l + 1 > len(s1) or (s2[r] in count and count[s2[r]] == 0):
    #         if s2[l] in count:
    #             count[s2[l]] += 1
    #         l += 1
    #     if s2[r] not in count:
    #         if s2[l] in count:
    #             count[s2[l]] += 1
    #         l += 1
    #     else:
    #         count[s2[r]] -= 1
        
    #     r += 1
    #     isSub = True

    #     print(count)

    #     for value in count.values():
    #         if value != 0:
    #             isSub = False
    #             break

    #     if isSub == True:
    #         return True

    # return False

print(checkInclusion("adc", "dcda"))