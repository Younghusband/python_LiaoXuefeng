# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
# 过于简单。。。
from collections import *


def p(it):
    if not isinstance(it, Iterable) or isinstance(it, str):
        print(it)
    else:
        for x in it:
            print(x, end = '\t')
    print()


def huiFilter(i):
    s = str(i)
    return s == s[::-1]


L = [12321, 1222, 32123]

p(filter(huiFilter, L))
