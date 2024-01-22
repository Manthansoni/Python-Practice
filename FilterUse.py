from functools import reduce
my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))


# zip function use
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))

# Reduce Function


my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
