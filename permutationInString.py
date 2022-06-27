
# morning algos
# neetcode permutation in string, check inclusion

# failed to complete
# neetcode solution was not very helpful
# i think if i try again i can come up with a working more understandable solution to this algo

def checkInclusion(s1, s2):
    # first turn s1 into a dictionary
    # run a window using l and r pointers through s2

    # if something doesn't match like letter isnt in dict or too many
    # add s[l] back and increment l
    letter_dict = {}
    output = False
    for i in range(len(s1)):
        if s1[i] not in letter_dict:
            letter_dict[s1[i]] = 1
        else:
            letter_dict[s1[i]] += 1

    print(letter_dict)

    l = 0
    for r in range(len(s2)):
        if s2[r] not in letter_dict:
            while s2[l] in letter_dict:
                letter_dict[s2[l]] += 1
                l += 1
            l += 1
            continue
        else:
            letter_dict[s2[r]] -= 1
        
        if not any(letter_dict.values()):
            print(letter_dict)
            output = True
            break
        elif letter_dict[s2[r]] < 0:
            if s2[l] in letter_dict:
                letter_dict[s2[l]] += 1
            l += 1
    print(letter_dict)

    return output

print(checkInclusion("adc", "dcda"))