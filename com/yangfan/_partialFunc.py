# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样

x = int('12345', base = 8)  # 表示左侧的字符串是8进制的数字
print(x)  # 转换成10进制的相应结果

x = int('12345', base = 16)
print(x)  # 同上


# 转换2进制字符串 到十进制数字
def int2(x, base = 2):
    return int(x, base)


x = int2('1011011')
print(x)
print('---------partial below----------')
# -------------------functools.partial-----------------------

import functools

int3 = functools.partial(int, base = 2)
print(int3('11111'))
print(int3('11111', base = 8))  # partial后依旧可以传入其他值

# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

kw = {'base': 2}
print(int('10010', **kw))   # 这种等同于int('10010', base = 2)

max2 = functools.partial(max,10)  # 其实这么做没有什么意义，也就是调用max2的时候会默认在比较的范围内先插入一个10
args = (5,6,7)
print(max2(*args)) # 会打印10

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
# 可以理解为 def xxx( a= xxx, b = xxx ...)
