# Define a function is_palindrome() that recognizes palindromes
# (i.e. words that look the same written
# backwards). For example, is_palindrome("radar")
# should return True.

def reverse_str(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)


def is_palindrome(string1):
    reversed_str = reverse_str(string1)
    if reversed_str.__eq__(string1):
        return True
    else:
        return False


print(is_palindrome("radar"))


def is_reverse(string2):
    str_rev = ''
    for s in string2:
        str_rev = s + str_rev

    return str_rev

def is_palindro(string3):
    reverse_1 = is_reverse(string3)
    if reverse_1 == string3:
        return True
    else:
        return False


print(is_palindro("radar"))
