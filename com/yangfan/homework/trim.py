# method1 正序遍历至非空 倒叙遍历至非空

# 以下是基础，需要理解而非记忆
L = [1, 2, 3, 4, 5, 6, 0]
print(L[:])     # 复制
print(L[1:])    # 左侧少一
print(L[:-1])   # 右侧少一
print(L[-1:])   # 最后一个
print(L[:1])    # 第一个


test1 = '  hell o ss  '
test2 = ''
test3 = ' '


def trim1(arg1):
    start = 0
    end = 0
    for n in arg1[::1]:
        if n == ' ':
            start += 1
        else:
            break
    for n in arg1[::-1]:
        if n == ' ':
            end -= 1
        else:
            break
    v = arg1[start:end]
    return v


print(trim1(test1))
print(trim1(test2))

print('------------- method2 -------------')


# method2  利用切片的特性
def trim2(arg1):
    # if arg1 == '':
    #     return arg1
    while arg1[:1] == ' ':
        arg1 = arg1[1:]
    while arg1[-1:] == ' ':
        arg1 = arg1[:-1]
    return arg1


print(trim2(test1))
print(trim2(test2))

# ---------------------
