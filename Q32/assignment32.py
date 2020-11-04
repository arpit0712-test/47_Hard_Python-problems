# Write a version of a palindrome recogniser that accepts
# a file name from the user, reads each line, and
# prints the line to the screen if it is a palindrome.

from Q17 import assignment17
from Q17.assignment17 import palindrome_string


def palindrome_text():
    file = open('sample.text', 'r+')
    for word in file.read().split("\n"):
        if palindrome_string(word):
            print(word)


print(palindrome_text())
