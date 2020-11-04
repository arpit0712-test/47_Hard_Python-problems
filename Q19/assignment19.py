# "99 Bottles of Beer" is a traditional song in the United States and Canada.
# It is popular to sing on long trips,
# as it has a very repetitive format which is easy to memorize,
# and can take a long time to sing. The song's
# simple lyrics are as follows:
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.
# The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or
# singers reach zero.
# Your task here is write a Python program capable of generating all the verses of the song.

def beerBottle():
    for i in range(99, 0, -1):
        print(str(i) + " bottles of beer on the wall ", str(i) + " bottles of beer")
        print("Take one down, pass it around," + str(i - 1) + " bottles of beer on the wall.")
        print("  ")


beerBottle()


def beerBottle2(counter):
    while counter > 0:
        print(str(counter) + " bottles of beer on the wall ", str(counter) + " bottles of beer")
        print("Take one down, pass it around," + str(counter - 1) + " bottles of beer on the wall.")
        print("  ")
        counter = counter - 1
    return counter


print(beerBottle2(99))
