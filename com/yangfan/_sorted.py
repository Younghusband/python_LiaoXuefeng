# 练习python内置sorted() 的用法
# 感觉sorted 里面其实是使用了类似map的东西，在key= 函数
# 区别在于map会改变原有数据，sorted只会排序不会改变数据
from collections import *
def p(it):
    if not isinstance(it, Iterable) or isinstance(it, str):
        print(it)
    else:
        for x in it:
            print(x, end = '\t')
    print()


r = sorted([36, 5, -12, 9, -21])
print(isinstance(r, Iterable))
print(isinstance(r, Iterator))
print(isinstance(r, list))
print(isinstance(r, str))
print(r)

#----- 传入 key 函数

r = sorted([36, 5, -12, 9, -21], key = abs)  # 按照绝对值大小排序 但并不改变值
print(r)
r = sorted(map(abs,[36, 5, -12, 9, -21]))  # 将数组变成绝对值数组 然后排序
print(r)

#----- 字符排序 默认按照ASCII码  但是 A-Z,a-z 这样不符合我们实际的需求
r = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(r)
r = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower)  # 这样就会严格按照字母顺序排序了
print(r)
r = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse=True)  # 逆序
print(r)
