from collections import *

# 打印的方法
def p(it):
    if not isinstance(it, Iterable):
        raise AttributeError
    for x in it:
        print(x, end = '\t')
    print()