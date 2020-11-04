# Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user,
# builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted
# character frequency table to the screen.

def char_freq_table():
    file = open('sample.text', 'r')
    chars = file.read().lower().replace(" ", "").replace("\n", "")
    freqs = {key: 0 for key in chars}
    for char in chars:
        freqs[char] += 1

    for key, value in freqs.items():
        print(key, " ", value)


print(str(char_freq_table()))
