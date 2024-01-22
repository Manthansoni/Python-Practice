# Square
list1 = [5, 4, 3]

print(list(map(lambda item: item ** 2, list1)))

# List Sorting
list2 = [(0, 2), (4, 3), (9, 9), (10, -1)]

list2.sort(key=lambda x: x[1])
print(list2)
