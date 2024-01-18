print("Hello world")

# String indexing
got = "HELLO"
a = got[2]
b = got[-2]
print(len(got))
print("a : " + a)
print("b : " + b)

# Slicing strings
c = got[:4]  # from start to index 3 (not included)
d = got[1:]   # from index 1 till the end of string
e = got[:-1]  # from start till the second last character
f = got[-4:-1]  # from the fourth last char till the second last one
g = got[::2]  # with a step of 2, it prints every second letter
h = got[::-1] # reverse the string
print("c : " + c)
print("d : " + d)
print("e : " + e)
print("f : " + f)
print("g : " + g)
print("h : " + h)


