# 测试"返回函数"  就是函数里面return 另一个函数
def calc_sum(*args):
    s = 0
    for n in args:
        s = s + n
    return s


def lazy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s = s + n
        return s

    return sum  # 如果这里 return sum() 下面的结果截然不同


f = lazy_sum(1, 3, 5, 7, 9)

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)

print(f1 == f2) # return sum的话是False, return sum()的话是True


# 闭包  返回函数的内部引用了外部的局部变量

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)        # 可以理解为每次append进去的不是i*i 而是一个尚未返回的函数的引用
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())  # 打印三行 9

#  ！！！ 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def count(*args):
    def f(j):
        def g():
            return j * j
        return g        # 用一个f函数包装一下g函数的输出 调用f函数的时候g已经返回了
    result = []
    for n in args:
        result.append(f(n))
    return result


f1, f2, f3 = count(1, 3, 5)
print(f1())
print(f2())
print(f3())