# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the
# numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1,
# 2, 3, 4]) should return 24
from functools import reduce


def sum_of_list(list1):
    list_sum = 0
    for i in list1:
        list_sum = list_sum + i
    print(list_sum)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_list(list1)


def product_of_list(list1):
    list_prod = 1
    for i in list1:
        list_prod = list_prod * list1[i - 1]
    print(list_prod)


product_of_list(list1)


def func_sum():
    print(sum(list1))


func_sum()


def multiple(list1):
    result = reduce((lambda x, y: x * y), list1)
    print(result)


multiple(list1)


