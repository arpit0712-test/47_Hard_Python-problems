# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if then­else
# construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is
# nevertheless a good exercise.)

def max_num(num1, num2):
    if num1 > num2:
        print("Number greater is", num1)
    else:
        print("Number greater is", num2)


max_num(2, 5)


def max_num1(num1, num2):
    result = max(num1, num2)
    print("Number greater is ", result)


max_num1(23, 45)


def max_num_list(list1):
    max_number = list1[0]
    for i in list1:
        if i > max_number:
            max_number = i
    return max_number


list1 = [2, 3, 4, 5, 6, 7, 7, 8, 19, 29, 0, 10]
print("Largest number", max_num_list(list1))


def max_list_num(list2):
    result2 = max(list2)
    print("max number in list", result2)


list2 = [2, 3, 4, 5, 6, 7, 7, 8, 19, 29, 0, 10]
max_list_num(list2)
