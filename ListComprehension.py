# For List

# my_list = [param for param in iterable]

my_list = [char for char in "Heloo"]
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]


print(my_list4)

# For Set

my_list = {char for char in "Heloo"}
my_list2 = {num for num in range(0, 100)}
my_list3 = {num**2 for num in range(0, 100)}
my_list4 = {num**2 for num in range(0, 100) if num % 2 == 0}

# For Dictionary

dict1 = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in dict1.items() if value % 2 == 0}

print(my_dict)


# Exercise

# List to dictionary

my_dict1 = {num: num*2 for num in [1, 2, 3]}

print(my_dict1)
