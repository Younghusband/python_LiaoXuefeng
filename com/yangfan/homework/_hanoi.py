# 汉诺塔
# move是正确的解法, 将上层的n-1块 和 最底层的一块 拆分开来。
# move是我条件反射的错误解法，将上层的1块 和 底层的n-1块 拆分开来。  仔细想一想错在哪

count = 0

def move(_n, _a, _b, _c):
    if _n == 1:
        print(_a, "-->", _c)
    else:
        move(_n - 1, _a, _c, _b)
        move(1, _a, _b, _c)
        move(_n - 1, _b, _a, _c)


def move1(n, A, B, C):
    if n == 1:
        print(A, "-->", C)
    else:
        move(1, A, C, B)
        move(n - 1, A, B, C)
        move(1, B, A, C)


move(4, 'A', 'B', 'C')
# move1(4, 'A', 'B', 'C')
print("------------")
# move(3, 'A', 'B', 'C')
