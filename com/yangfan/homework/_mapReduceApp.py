from collections import *
from functools import reduce


def p(s):
    if isinstance(s, Iterable):
        for x in s:
            print(x, end = ' ')
    else:
        print(s, end = '')
    print()


# 做这三道题目最大的感触就是，切片是很重要的工具，一定要想到使用切片


# homework1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

# 不要map嵌套map
def standardName(_namelist):
    if _namelist is None:
        return None

    def capitalUpper(s):  # 完成单个字符串过来返回首字母大写的字符串
        return s[:1].upper() + s[1:].lower()  # 由于这里s的类型是未知的，所以ide并不能提供给我们方法提示

    return map(capitalUpper, _namelist)


p(standardName(['adam', 'LISA', 'barT']))
p('--------Homework1 End--------')


# homework2
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(_list):
    def xx(x, y):
        return x * y

    return reduce(xx, _list)


p(prod([3, 5, 7, 9]))
p('--------Homework2 End--------')

# homework3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def getDigit(s):
    return DIGITS[s]


def str2float(_str):
    slist = _str.split('.')
    if len(slist) == 1:  # 不包含小数点
        return reduce(lambda x, y: x * 10 + y, map(getDigit, slist[0]))
    else:
        return reduce(lambda x, y: x * 10 + y, map(getDigit, slist[0] + slist[1])) / pow(10, len(slist[1]))

p(str2float('123.456'))
p('--------Homework3 End--------')

# p(str2float("123.456"))
p(len('yangfan'))
