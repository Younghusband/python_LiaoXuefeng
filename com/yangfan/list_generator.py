import os

O = []

for x in range(1, 11):
    O.append(x * x)

print(O)

print('-------------------------')

X = list(range(1, 11))

print(X)
print('-------------------------')

L = [x * x for x in range(1, 11)]

print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]

print('-------------------------\n', L)

L = [x + y for x in 'ABC' for y in 'XYZ']

print('-------------------------\n', L)


[d for d in os.listdir('.')]  # os.listdir可以列出文件和目录  虽然我不知道怎么打印。。

d = {'x': 'A', 'y': 'B', 'z': 'C'}

L = [k + '=' + v for k, v in d.items()]

print('-------------------------\n', L)

L = ['Hello', 'World', 'IBM', 'Apple']

L = [s.lower() for s in L]

print('-------------------------\n', L)

print(isinstance('ABC', str))
print(isinstance([], str))

