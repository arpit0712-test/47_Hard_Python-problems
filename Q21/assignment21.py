# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained
# in it. Represent the frequency listing as a Python dictionary. Try it with something like
# char_freq("abbabcbdbabdbdbabababcbcbab").

def character_freq(string1):
    dict1 = {}
    for i in string1:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1

    for key, value in dict1.items():
        print(key, " ", value)


print(character_freq("abbabcbdbadefghjijnhgcfvvbdbdbabababcbcbab"))


# def freq_char(string2):
#     dict2 = {}
#     for i in range(len(string2)):
#         if string2[i] in dict2:
#             dict2[string2[i]] = int(dict2.get([string2[i]])) + 1
#         else:
#             dict2[string2[i]] = 1
#     return dict2
#
#
# print(str(freq_char("aaabbcdbbebsjfjvntuwjhfklfjalhfsd")))
