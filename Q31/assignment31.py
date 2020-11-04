# Implement the higher order functions map(), filter() and
# reduce(). (They are builtin but writing
# them yourself may be a good exercise.


def map(function, iterable):
    results = []
    for i in iterable:
        results.append(function(i))
    return results


l = ['sat', 'bat', 'cat', 'mat']
print(map(list, l))


def filtered(function, iterable):
    return [i for i in iterable if function(i) == True]


list2 = [1, 2, 3, 4, 5]
print(filtered(max, list2))
