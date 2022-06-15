
# morning algos
# neetcode encode and decode strings

# this is a good solution and it works
# def encode(strs):
#     encoded_string = ""
#     rand_num = "4062839517"

#     for word in strs:
#         encoded_string += word
#         encoded_string += rand_num
#     return encoded_string

# def decode(str):
#     decoded_strings = []
#     rand_num = "4062839517"

#     while len(str) >=1 :
#         rand_num_index = str.find(rand_num)
#         decoded_strings.append(str[:rand_num_index])
#         str = str[rand_num_index + 10:]

#     return decoded_strings

# lets come up with something safer though...
def encode(strs):
    encoded_string = ""
    

    for word in strs:
        word_length = str(len(word))
        encoded_string += word_length + "#" + word
    return encoded_string

def decode(str):
    decoded_strings = []

    i = 0
    while len(str) > 0:
        if str[i].isdigit() and str[i+1] == "#":
            idx_end_of_word = int(str[i])
            decoded_strings.append(str[2:2+idx_end_of_word])
            str = str[2+idx_end_of_word:]
            i = 0
        else:
            i += 1

    return decoded_strings

encoded_string = encode(["Let's", "code", "some", "code"])
print(decode(encoded_string))

