# fibonacci


def feb(x):
    n, a, b = 0, 1, 1
    while n < x:
        print(a)
        a, b = b, a + b
        n += 1
    return 'Done'


print(feb(3))

print('-----------------------------')


# -----------------------------------


def feb_generator(x):
    n, a, b = 0, 1, 1
    while n < x:
        yield a
        a, b = b, a + b
        n += 1
    return 'Done'


for n in feb_generator(6):
    print(n)

# f = feb_generator(6)   # 相同的作用
# for n in f:
#     print(n)

# -----------接下来试着捕捉yield返回的值-----------
print('-------------------------')

g = feb_generator(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generate return value:', e.value)
        break

