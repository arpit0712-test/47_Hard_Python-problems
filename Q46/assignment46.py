# An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same
# order as the original word, make up at least two other words. All letters must be used, but the smaller words
# are not necessarily of the same length. For example, a word with seven letters where every second letter is
# used will produce a four­letter word and a three­letter word

fileIn = open('sample.text', 'r+')
for line in fileIn:
    line = line.strip()
    length = len(line)
    word1 = ""
    word2 = ""
    for i in range(0, length, 2):
        word1 += line[i]
        try:
            word2 += line[i + 1]
        except:
            pass
        word1 = word1.strip()
        word2 = word2.strip()
        print("==>", word1, "and", word2)
