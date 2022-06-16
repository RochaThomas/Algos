
# morning algos
# neet code valid palindrome

# works but its slow
# def isPalindrome(s):

#     s = s.lower()

#     for c in s:
#         if not c.isalpha() and not c.isdigit():
#             s = s.replace(c,'')

#     print(s)

#     for i in range(int(len(s)/2)):
#         if s[i] != s[len(s) - 1 - i]:
#             return False
    
#     return True

    # r a c e c a r
    # 0 1 2 3 4 5 6
    #       ! 

# second try with two pointers
# faster

def isPalindrome(s):
    front = 0
    back = len(s) - 1

    while front <= back:

        if s[front].isalnum():
            if s[front].isalpha() and s[front].isupper():
                s = s.replace(s[front], s[front].lower())
        else:
            front += 1
            continue

        if s[back].isalnum():
            if s[back].isalpha() and s[back].isupper():
                s = s.replace(s[back], s[back].lower())
        else:
            back -= 1
            continue

        if s[front] != s[back]:
            return False
        else:
            front += 1
            back -= 1
    return True

print(isPalindrome("0P"))