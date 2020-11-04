# Write a program that given a text file will create a new text file in which
# all the lines from the original file are
# numbered from 1 to n (where n is the number of lines in the file)
import re


def stringNumber():
    file = open('sample.text', 'r+')
    words = re.findall('\w+', file.read())
    fileout = open('result.text', 'w+')
    for line, context in enumerate(words):
        fileout.write('%s %s ' % (line + 1, context))

    fileout.close()


print(stringNumber())
