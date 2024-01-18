
def highest_even(li):
    high = 0
    for items in li:
        if items % 2 == 0:
            if high < items:
                high = items
    return(high)

print(highest_even([10,2,3,4,8,12,46]))

# 2nd approach
def highest_even(li):
    even = []
    for items in li:
        if items % 2 == 0:
            even.append(items)
    return(max(even))

print(highest_even([10,2,3,4,8,12,46]))