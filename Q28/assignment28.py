# Write a function find_longest_word() that takes a list of words and
# returns the length of the longest
# one. Use only higher order functions
from functools import reduce


def length_of(list1):
    return max(map(len, list1))


list1 = ['ok', 'three', 'worker', 'sssssssss']
print(length_of(list1))

