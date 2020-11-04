# map , reduce , filter , lembda , list comprehension

# 1) map

def sum_of_list(list1):
    sumOf = 0
    for i in list1:
        sumOf = sumOf + i
    return sumOf


list1 = [1, 2, 3, 4, 5, 6, 7]
sum_tot = list(map(sum_of_list, list1))
print(sum_tot)
