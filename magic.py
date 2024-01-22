# Magician Game

# If magician AND expert : "you are master"
# If magician but not expert : "at least getting there"
# If not magician : "You need magic powers"

is_magician = False
is_expert = False

if is_magician and is_expert:
    print("You are master")
elif is_magician and not is_expert:
    print("At least getting there")
elif not is_magician:
    print("You need magic powers")


# # Counter
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
# for item in my_list:
#     sum += item

# print(sum)


# for item in range(1, 5):
#     print(item)

# for _ in range(1, 10, 2):
#     print(_)

# for _ in range(1, 10, 2):
#     print(list(range(1, 10)))

# for i, char in enumerate("Hellooo"):
#     print(i, char)

# i = 0
# while 50 < 50:
#     print(i)
#     i += 1
# else:
#     print("idk")

# while True:
#     response = input("Say Something : ")
#     if (response == 'bye'):
#         break


# Exercise

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for image in picture:
    for pixel in image:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('\n')


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dup = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in dup:
            dup.append(value)

print(dup)

# using comprehensions

dupli = list(set([x for x in some_list if some_list.count(x) > 1]))
print(dupli)
