# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

L = [5, 3, 2, 1, 8, 6, 7]


def find_return(list1):
    if list1 == []:
        return None, None
    mi, ma = None, None
    for v in enumerate(list1):
        if mi is None or v < mi:  # is None一定要放在前面，否则None值是无法比较大小的
            mi = v
        if ma is None or v > ma:
            ma = v
    return mi, ma  # 自动返回tuple


print(find_return(L))
print(find_return([]))
print('---------------改写---------------')


def find_return_pro(list1):  # 改进版 初始化时避免了None
    if list1 == []:
        return None, None
    mi, ma = list1[0], list1[0]
    for v in enumerate(list1):
        if v < mi:  # is None一定要放在前面，否则None值是无法比较大小的
            mi = v
        if v > ma:
            ma = v
    return mi, ma  # 自动返回tuple


print(find_return_pro(L))
print(find_return_pro([]))
