# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a
# salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet
# ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote
# sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually
# ignored
import re


def palindrome_string(string1):
    string1 = re.sub('[^a-zA-Z0-9]', '', string1)
    reveres = string1[::-1]
    if string1.lower() == reveres.lower():
        return True
    else:
        return False


string1 = "Go hang a salami"
string2 = "Was it a rat I saw?"
string3 = "Step on no pets"
string4 = "Sit on a potato pan, Otis"
string5 = "Lisa Bonet ate no basil"
string6 = "Satan, oscillate my metallic sonatas"
string7 = "I roamed under it as a tired nude Maori"
string8 = "Rise to vote sir"
string9 = "Dammit, I'm mad!"

# print(palindrome_string(string1))
# print(palindrome_string(string2))
# print(palindrome_string(string3))
# print(palindrome_string(string4))
# print(palindrome_string(string5))
# print(palindrome_string(string6))
# print(palindrome_string(string7))
# print(palindrome_string(string8))
# print(palindrome_string(string9))
