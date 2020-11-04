# Write a function find_longest_word() that takes a
# list of words and returns the length of the longest
# one
#
def find_longest_word():
    list_of_words = ['ok', 'three', 'jackal', 'mango']
    list_of_sizes = []
    for i in list_of_words:
        list_of_sizes.append(len(i))
    return max(list_of_sizes)


print("Size of longest word", find_longest_word())


def find_longest_words():
    list_of_words = ['ok', 'three', 'jackal', 'mango']
    # list_of_sizes = []
    max_wrd = 0
    longest_word = ""
    for word in list_of_words:
        if len(word) > max_wrd:
            max_wrd = len(word)
            longest_word = word
    return longest_word


print(find_longest_words())


def find_longest_word2():
    list_of_words = ['ok', 'three', 'jackal', 'mango']
    list_of_sizes = []
    for i in range(len(list_of_words)):
        list_of_sizes.append(len(list_of_words[i]))
    return list_of_sizes


def find_max_size():
    size_list = find_longest_word2()
    max_size = size_list[0]
    for i in size_list:
        if i > max_size:
            max_size = size_list[i]
    return max_size

# print(find_max_size())
