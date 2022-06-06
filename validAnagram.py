


def isAnagram(word, test_word):
    letter_dict = {}

    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1


    for letter in letter_dict:
        count = 0
        for i in range(len(test_word)):
            if test_word[i] == letter:
                count += 1

        if count != letter_dict[letter]:
            return False
    
    word_set = set(word)
    test_word_set = set(test_word)

    if len(word_set) != len(test_word_set):
        return False

    # count = 0
    # for i in range(len(test_word)-1):
    #     if test_word[i] in letter_dict:
    #         for letter in test_word:
    #             if letter == test_word[i]:
    #                 count += 1
    #         if count != letter_dict[test_word[i]]:
    #             return False
    #         count = 0
    #     else:
    #         return False

    return True

print(isAnagram("anagram", "znagaram"))