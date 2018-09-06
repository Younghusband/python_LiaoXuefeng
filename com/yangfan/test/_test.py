def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# g = fib(6)
#
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break


from collections import Iterator
from collections import Iterable

print(isinstance(range(1, 10), Iterable))


def f(x):
    return str.lower(x)


r = map(f, ['A', 'B', 'C', 'D'])

for x in r:
    print(x, end = '\t')


