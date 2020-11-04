# Write a program that maps a list of words into a list of integers representing the lengths of the correponding
# words. Write it in three different ways: 1) using a for loop, 2) using the higher order function map(), and 3)
# using list comprehensions.


# 1) using for loop
def word_map():
    list1 = []
    list2 = ['one', 'ok', 'the', 'four', 'seven']

    for i in range(len(list2)):
        list1.append(len((list2[i])))

    print("list of words ", list2)
    print("length of words", list1)


word_map()


# higher order function

def word_map2(list1):
    return map(len, list1)


list1 = ['one', 'ok', 'the', 'four', 'seven']
print(list(word_map2(list1)))


def word_map3(list2):
    return [len(i) for i in list1]


print(word_map3(list1))
