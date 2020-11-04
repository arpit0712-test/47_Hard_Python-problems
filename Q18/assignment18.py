# A panagram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog.
# Your task here is to write a function to check a sentence to see if it
# is a pangram or not

def isPanagram(str):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabets:
        if char not in str.lower():
            return False
    return True


print(isPanagram("The quick brown fox jumps over a lazy dog"))

import string
alphabet = set(string.ascii_lowercase)
# string.ascii_lowercase : this method in the string is to

def panacheck(string):
    return set(string.lower()) >= alphabet


print(panacheck("The quick brown fox jumped on the lazy dog"))
