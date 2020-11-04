# Define a function that computes the length of a given list or string.
# (It is true that Python has the len()
# function built in, but writing it yourself
# is nevertheless a good exercise.)

# using counter to find length
def string_length(str):
    counter = 0
    for i in str:
        counter = counter + 1
    return counter


print(string_length("arpit"))


# using function to find length
def length_of_string(str):
    print(len(str))


length_of_string("Arpit")


# using while loop to find the length
def string1(str):
    count = 0
    while str[count:]:
        count += 1
    return count


str = "fox jumped"
print(string1(str))


def lenOfString(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return (some_random_str.join(str)).count(some_random_str) + 1


str = "quick brown fox"
print(lenOfString(str))
