# Define a procedure histogram() that takes a list of integers and
# prints a histogram to the screen. For
# example, histogram([4, 9, 7])
def histogram(list1):
    for i in range(len(list1)):
        print(list1[i] * "x")


list1 = [14, 13, 16]
histogram(list1)


# def generate_n_chars(n, c):
#     output = ""
#     for i in range(n):
#         output = output + c
#     return output
#
#
# def histo(list2):
#     for i in range(len(list2)):
#         res = generate_n_chars(len(list2[i]), 'c')
#         return res


list2 = [3, 4, 5]
print(histo(list2))
