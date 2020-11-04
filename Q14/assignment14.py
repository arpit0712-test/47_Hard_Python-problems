# Write a program that maps a list of words into a list of
# integers representing the lengths of the corresponding
# words.

def match_len_to_words():
    listOfsizes = []
    list_words = ['I', 'ok', 'the', 'four', 'fives']
    for i in range(len(list_words)):
        listOfsizes.append(len(list_words[i]))

    print("List of words ", list_words)
    print("List of sizes of each word ", listOfsizes)


print(match_len_to_words())
