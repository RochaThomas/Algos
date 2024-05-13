
# morning algos
# neetcode permutation in string, check inclusion

def checkInclusion(s1, s2):
    if not s1: return True
    if len(s1) > len(s2): return False

    
    s1Letters, s2Letters = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Letters[ord(s1[i]) - ord('a')] += 1
        s2Letters[ord(s2[i]) - ord('a')] += 1
    matches = 0
    for i in range(26):
        matches += (1 if s1Letters[i] == s2Letters[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True
        index = ord(s2[r]) - ord('a')
        s2Letters[index] += 1
        if s1Letters[index] == s2Letters[index]:
            matches += 1
        elif s1Letters[index] + 1 == s2Letters[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Letters[index] -= 1
        if s1Letters[index] == s2Letters[index]:
            matches += 1
        elif s1Letters[index] - 1 == s2Letters[index]:
            matches -= 1
        l += 1
    return matches == 26


print(checkInclusion("adc", "dcda"))