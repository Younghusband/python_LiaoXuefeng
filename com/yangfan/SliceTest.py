L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print([L[1], L[2]])  # slice

n = 3
r = []
for i in range(0, n, 1):  # 含头不含尾，步长为1
    r.append(L[i])

print(r)

print(L[0:3])
print(L[:3])

N = list(range(100))

print(N[::])
print(N[:10])  # 冒号前面是头，后面是尾  取出来的内容含头不含尾
print(N[-10:])  # 倒着取10个数
print(N[10:20])  # 含10 不含20
print(N[:10:2])  # 不含10 步长为2 从0开始取
print(N[::5])  # 不设边界，步长为5

tu = (0, 1, 2, 3, 4, 5)[::2]
print(tu)
tu = 'ABCDEFG'[:3]
print(tu)

# 利用切片实现trim操作


print('' == '')
print('' is '')  # 好像这两种方式都能判断字符串相等


# 思路: 正序遍历找到第一个不是' '的字符记录index ,倒序遍历找到第一个不是' '的字符记录index

def trim1(str1):
    start = 0
    end = 0
    for c in str1[::1]:  # 正序遍历
        if c == ' ':
            start += 1
        else:
            break
    for x in str1[::-1]:  # 倒序遍历
        if x == ' ':
            end -= 1
        else:
            break
    v = str1[start:end]
    return v


str2 = '    hel lo  '
print(trim1(str2))
