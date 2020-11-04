def max_num_list(list1):
    max_number = list1[0]
    for i in list1:
        if i > max_number:
            max_number = i
    return max_number


list1 = [2, 3, 4, 5, 6, 7, 7, 8, 19, 29, 0, 10]
print("Largest number", max_num_list(list1))


def max_list(list2):
    return max(list2)


print(max_list(list1))

# net solution

def list_max(inputList):
    sortedList = sorted(inputList)
    return sortedList[-1]


print(list_max(list1))
