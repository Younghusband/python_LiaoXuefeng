def myabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x > 0:
        return x
    else:
        return -x


print(myabs(-3))
# print(myabs("A"))

str1 = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

str1 = str1[2:-1]

print(str1)
