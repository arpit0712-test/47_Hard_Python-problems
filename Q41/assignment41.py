# In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word
# by guessing, and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to
# identity as well as to position, and 2) the characters that are indeed present in the word, but which are
# placed in the wrong position. Write a program with which one can play Lingo. Use square brackets to mark
# characters correct in the sense of 1), and ordinary parentheses to mark characters correct in the sense of
# 2).

target = 'tiger'
input1 = input('Enter words')

while input1 != target:
    output = ''
    for pos, char in enumerate(input1):
        if char in target:
            if target[pos] == input1[pos]:
                output += '[' + char + ']'
            else:
                output += '(' + char + ')'
        else:
            output += char
    print("Clue:" + output)
    input1 = input('')
print("Found")
