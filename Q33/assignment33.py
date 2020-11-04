# According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. (
# "Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (
# pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilapsto the
# screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair
# "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!

def semilindrop():
    file = open('sample2.text', 'r+')
    words = file.read().split()
    results = []
    for word in words:
        for word2 in words:
            if word == word2[::-1]:
                results.append(word)
    return results


print(str(semilindrop()))
