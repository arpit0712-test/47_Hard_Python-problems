# Using the higher order function filter(),
# define a function filter_long_words() that takes a list of
# words and an integer n and returns the list of words that are longer than n

def filter_long_words(list1, n):
    list2 = []
    for i in list1:
        if len(i) > n:
            list2.append(i)
    return list2


list1 = ['aa', 'bb', 'dcdcdcdcdc', 'wdwwdwd', 'ss', 'xszz']
print(filter_long_words(list1, 3))


# higher order function

def filter_filter(words, n):
    return filter(lambda x: len(x) > n, words)


words = ['aa', 'bb', 'dcdcdcdcdc', 'wdwwdwd', 'ss', 'xszz']
print(list(filter_filter(words, 3)))
