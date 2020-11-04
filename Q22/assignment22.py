# In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text
# is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A
# would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who
# used it to communicate with his generals. ROT­13 ("rotate by 13 places") is a widely used example of a
# Caesar cipher where the shift is 13. In Python, the key for ROT­13 may be represented by means of the
# following dictionary:
import re


def cipher(inputString):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
           'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
           'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j',
           'x': 'k',
           'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
           'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z',
           'N': 'A',
           'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H',
           'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    newString = ""
    for word in (re.findall('[a-zA-Z0-9?!]+', inputString)):
        for j in range(len(word)):
            if word[j] in key:
                newString = newString + key[word[j]]
            else:
                newString = newString + word[j]
        newString = newString + " "
    print(newString)


cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")
cipher("I have the card come and take it from me")
