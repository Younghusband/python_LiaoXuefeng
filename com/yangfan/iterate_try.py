# coding=utf-8 练习一下python的迭代
from collections import Iterable

L = list(range(1, 5))  # 含头不含尾 1到4

for i in L:
    print(i, ', ', end = '')

d = {'a': 1, 'b': 2, 'c': 3}

for i in d:  # 默认迭代的是dict的key
    print(i, ', ', end = '')

for i in d.values():  # 迭代的是value
    print(i, ', ', end = '/')

for i in d.items():  # 这样打印出来的每个元素都是(k,v)
    print(i, ', ', end = '->')

for k, v in d.items():
    print(k, ",", v, ".", end = "|\n")

print('-------------------------------------------------')

# ------------------------

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

# 判断一个对象是可迭代对象


print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))  # false

# enumerate

for index, value in enumerate(['a', 'c', 'dd']):  # 这样就会有下标了。
    print(index, '->', value)

