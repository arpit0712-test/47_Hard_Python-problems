# Write a function filter_long_words() that takes a list of words
# and an integer n and returns the list of
# words that are longer than n.

def filter_long_words(num, listOfWords):
    out_list = []
    for word in listOfWords:
        if len(word) > num:
            out_list.append(word)
    return out_list


listOfWords = ['ok', 'Thress', 'bolkat', 'servers', 'ss', 's']
print(filter_long_words(2, listOfWords))

