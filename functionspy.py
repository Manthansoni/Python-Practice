def sum1(n1, n2):
    '''
    Info: it will return n1 + n2
    '''
    # above will be shown when we will define the function and on hover it describes the info
    return n1+n2


print(sum1(10, 5))

print(sum1.__doc__)
help(sum1)


def sum2(n1, n2):
    '''
    sum1
    '''
    def ano_sum(n1, n2):
        return n1 + n2
    return ano_sum(n1, n2)


total = sum1(10, 20)

print(total)

# default function
# keyword functions
# *args and **kwargs


def sum_more(*args):
    '''
    sum_more
    '''
    return sum(args)


print(sum_more(1, 2, 3, 4, 5))

# **kwargs


def sum_more1(**kwargs):
    '''
        sum_more1
    '''
    total = 0
    for items in kwargs.values():
        total += items
    return total


print(sum_more1(n1=1, n2=2, n3=3, n4=4, n5=5))

# Rule: params, *args, default parameters,**kwargs
