# Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers
# and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well
# call the reduce() function directly?
from functools import reduce


def max_in_list(list1):
    return reduce(max, list1)


list1 = [2, 3, 4, 5, 6, 7, 8, 9]
print(max_in_list(list1))


def max_in_list1(list1):
    output = reduce(lambda x, y: x if x > y else y, list1)
    return output


print(max_in_list1(list1))
