# Write a function is_member() that takes a value (i.e. a number, string, etc)
# x and a list of values a, and
# returns True if x is a member of a, False otherwise.
# (Note that this is exactly what the in operator does,
# but for the sake of the exercise you should pretend
# Python did not have this operator.)

def is_member(z, list1):
    if z in list1:
        return True
    else:
        return False


list1 = [1, 2, 3, 4, 5, 6]
print(is_member(6, list1))


def member_val(checkVal, list2):
    for i in range(len(list2)):
        if checkVal == list2[i]:
            return True


list2 = [1, 2, 3, 4, 5, 6]
print(member_val(4, list2))


def mem_val(chek, list3):
    for i in range(0, list3):
        if list3.count(chek) > 0:
            return True


list3 = [1, 2, 3, 4, 5]
chek = 3
print(member_val(chek, list3))
