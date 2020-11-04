# Write a function that takes a character (i.e. a string of length 1)
# and returns True if it is a vowel, False
# otherwise

def character_Search(chr):

    if (chr.__eq__('a') | (chr.__eq__('A'))) | (chr.__eq__('e') | (chr.__eq__('E'))) | (
            chr.__eq__('i') | (chr.__eq__('I'))) | (chr.__eq__('o') | (chr.__eq__('O'))) | (
            chr.__eq__('u') | (chr.__eq__('U'))):
        return True
    else:
        return False


print(character_Search('A'))

def find_character(x):
    if (x == 'a' or x == 'A' or x == 'e' or x == 'E' or x == 'i' or x == 'I' or x == 'o' or
            x == 'O' or x == 'u' or x == 'U'):
        return True
    else:
        return False


print(find_character('A'))
print(find_character('a'))
print(find_character('c'))






