# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    a = [0]         # 好奇a的生命周期什么时候结束
    # a = 0  # 配合下面的nonlocal a
    def counter():
        # nonlocal a
        a[0] += 1
        return a[0]
    return counter

f = createCounter()

print(f())
print(f())
print(f())
print(f(),end = '\n---- 以下是利用yield获得计数器 ----\n')


# ---------------- 利用yield来实现counter --------------


def counter():
    def count():
        n = 1
        yield n
        while True:
            n += 1
            yield n
    o = count()
    def getnext():
        return next(o)
    return getnext

xx = counter()   # counter() 一次性将getnext的函数引用返回。
                # 之后每次调用实际上走的是getnext而无关counter了

print(xx())
print(xx())
print(xx())
print(xx())


# --------------- 利用 generator --------------
def createCounter1():
    x = (x for x in range(1, 100))
    def counter():
        return next(x)
    return counter
