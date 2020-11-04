# Define a function overlapping() that takes two lists and returns True if they have at least one member in
# common, False otherwise. You may use your is_member() function, or the in operator, but for the sake
# of the exercise, you should (also) write it using two nested for loops

def overlapping():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [2, 7, 5, 4, 3, 0]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return True


print(overlapping())


def overlap():
    list3 = [3, 4, 5, 6, 7, 8, 9]
    list4 = [12, 3, 2, 55, 66, 77, 88]
    for i in range(len(list3)):
        for j in range(len(list4)):
            if list3[i].__eq__(list4[j]):
                return True


def overlap2():
    list5 = [1, 2, 3]
    list6 = [2, 5, 4]
    for i in list5:
        if i in list6:
            return True


print(overlap2())

print(overlap())
