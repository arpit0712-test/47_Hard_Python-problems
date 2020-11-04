# Write a program that will calculate the average word length
# of a text stored in a file (i.e the sum of all the
# lengths of the word tokens in the text,
# divided by the number of word tokens
import re


def averageStringsize():
    fileIn = open('sample.text', 'r+')
    words = re.findall('\w+', fileIn.read())
    return sum([len(word) for word in words]) / len(words)


# print(averageStringsize())


def wordAvgSize():
    fileIn = open('sample.text', 'r+')
    summ = 0
    avg = 0
    wordss = re.findall('\w+', fileIn.read())
    for word in wordss:
        summ = summ + (len(word))
        print(summ)
        avg = summ / len(wordss)
    return avg


print(wordAvgSize())
