# Write a program able to play the "Guess the number" game, where the number to be guessed is randomly
# chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a
# terminal:
import random


def NumberGuess():
    name = input("What is your name \n")
    print("Well" + name + "I am thinking of a number between 1 and 20")
    random_num = random.randint(1, 20)
    number = int(input("Enter the guess"))
    count = 1

    while number != random_num:
        if number < random_num:
            print("Guess too low")
        elif number > random_num:
            print("Guess too high")
        number = int(input("Take a guess"))
        count += 1

    print("Good you guessed the number is %d guess" % (count))


NumberGuess()
