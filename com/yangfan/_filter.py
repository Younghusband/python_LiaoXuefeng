# 高阶函数 filter 相关的笔记
from collections import *


def p(it):
    if not isinstance(it, Iterable) or isinstance(it, str):
        print(it)
    else:
        for x in it:
            print(x, end = '\t')
    print()


def is_odd(n):
    return n % 2 == 0  # 偶数才会存留


r = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8])

p(r)


# ---------------

def not_empty(s):
    return s and s.strip() # 这个我不是很理解

p(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

# --------------- 素数 筛选器 ---------------

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
