# 汉诺塔
# move是正确的解法, 将上层的n-1块 和 最底层的一块 拆分开来。
# move是我条件反射的错误解法，将上层的1块 和 底层的n-1块 拆分开来。  仔细想一想错在哪

count = 0


def move(n, A, B, C):
    global count
    if n == 1:
        count += 1
        print(A, "-->", C)
    else:
        move(n - 1, A, C, B)
        move(1, A, B, C)
        move(n - 1, B, A, C)


def move1(n, A, B, C):
    if n == 1:
        print(A, "-->", C)
    else:
        move(1, A, C, B)
        move(n - 1, A, B, C)
        move(1, B, A, C)


move(3, 'A', 'B', 'C')
print("------------")
print(count, '次移动')
# move1(4, 'A', 'B', 'C')
# move(3, 'A', 'B', 'C')
