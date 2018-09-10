# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

# 使用匿名函数改造下面的代码:

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

from com.yangfan.util._myutil import *

p(L)