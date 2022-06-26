
# morning algos
# neetcode permutation in string, check inclusion

def checkInclusion(s1, s2):
    # first turn s1 into a dictionary
    # run a window using l and r pointers through s2

    # if something doesn't match like letter isnt in dict or too many
    # add s[l] back and increment l
    letter_dict = {}
    for i in range(len(s1)):
        if s1[i] not in letter_dict:
            letter_dict[s1[i]] = 1
        else:
            letter_dict[s1[i]] += 1

    print(letter_dict)

    l = 0
    for r in range(len(s2)):
        if s2[r] not in letter_dict:
            if s2[l]  in letter_dict:
                letter_dict[s2[l]] += 1
            l += 1
            continue
        else:
            letter_dict[s2[r]] -= 1
        
        if not any(letter_dict.values()):
            return True
        elif letter_dict[s2[r]] < 0:
            if s1[i] not in letter_dict:
                letter_dict[s1[i]] = 1
            l += 1

    return False

print(checkInclusion("ab", "eidboaooo"))