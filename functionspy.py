def sum(n1,n2):
    return(n1+n2)

print(sum(10,5))


def sum1(n1,n2):
    def ano_sum(n1,n2):
        return n1 + n2
    return ano_sum(n1,n2)

total = sum(10,20)
print(total)