# Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am
# testing") should return the string "gnitset ma I".

def string_reverse(string1):
    reverse_str = string1[::-1]
    return reverse_str


print(string_reverse("I am testing"))


def reverse_str1(string2):
    reverse_str2 = ""
    string_len = int(len(string2))
    for i in range(0, string_len):
        reverse_str2 = reverse_str2 + string2[-i - 1]

    print(reverse_str2)


reverse_str1("I am testing")


def reversedStr(string3):
    rev_str = ''
    for s in string3:
        rev_str = s + rev_str
    print(rev_str)


reversedStr("I am reverse")


def reversed_j(s):
    s1 = ''.join(reversed(s))
    return s1


print(reversed_j("I am testing"))


def rev_str(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)


print(rev_str("I am testing"))
