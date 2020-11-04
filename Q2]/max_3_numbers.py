# Define a function max_of_three() that takes three numbers as arguments and returns the largest of
# them


def max_3_numbers(a, b, c):
    if a > b & a > c:
        print("element greater", a)
    elif b > c:
        print("element greater", b)
    else:
        print("element greater", c)


max_3_numbers(12, 123, 54)


def max_of_three(a, b, c):
    print("max of three", max(a, b, c))


max_of_three(21, 43, 54)

