# the function which we only want to use once can be written using lambda function
# Syntax : lambda param: action(param)
from functools import reduce

my_list = [1, 2, 3]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc,item: acc+item, my_list, 10))
