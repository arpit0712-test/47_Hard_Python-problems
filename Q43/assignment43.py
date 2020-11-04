# An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a
# new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word
# list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that
# share the same characters that contain the most words in them

from collections import defaultdict


def anagram_finder(file_name):
    words = []
    with open(file_name, 'r') as f:
        for line in f:
            words.append(line.rstrip())

    anadict = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anadict[key].append(word)

    longestana = 0
    for anagram, anawords in anadict.items():
        if len(anawords) > longestana:
            longestana = len(anawords)

    for anagram, anawords in anadict.items():
        if len(anawords) > longestana - 1:
            print(anagram, anawords)


anagram_finder('unixdict.txt')
