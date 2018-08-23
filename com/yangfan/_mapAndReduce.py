from collections import *


def p(it):
    if not isinstance(it, Iterable):
        raise AttributeError
    for x in it:
        print(x, end = '\t')
    print()


# map 的用法

def f(x):
    return x * x


def f1(x):
    return str.lower(x)


# r = map(f, ['A', 'B', 'C', 'D'])
r = map(f1, ['A', 'B', 'C', 'D'])

p(r)
print('\n---------map end----------')
# reduce的用法
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


def f3(x, y):
    return x + y


r = reduce(f3, [1, 2, 3, 4, 5])

print(r)


def tensum(x, y):
    return 10 * x + y


L = [1, 2, 3, 4, 5]
r = reduce(tensum, L)
print(r)
print('-----用完后的L-----')  # 这种情况下reduce并不会使得L无法打印，和下面的情形相悖
p(L)


def char2num1(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


# 将map和reduce结合的用法
rInner = map(char2num1, '13579')
# rOutter = reduce(tensum, rInner)  # 如果执行完这句 rInner就无法遍历出来内容了，需要将这句话屏蔽
print('-------用完后的rInner-------')

# r = reduce(tensum, map(char2num, '13579'))  # 等于上面两行的作用

# print(rOutter)
# print(isinstance(rInner, Iterable))
p(rInner)

# ------------ 将上面的东西封装 ------------

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def char2num(x, y):
        return 10 * x + y
        pass

    def str2char(i):
        return DIGITS[i]

    return reduce(char2num, map(str2char, s))


print(str2int('873432'))

# ------------ 用lambda函数封装 ---------------

reduce(lambda x, y: 10 * x + y, map(char2num1, '234234'))  # lambda 略
