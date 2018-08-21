# 普通递归
def calc(_n):
    if _n == 1:
        return 1
    return _n * calc(_n - 1)


print(calc(5))


# 尾递归

def _calc(_temp, _product):
    if _temp == 1:
        return _product
    return _calc(_temp - 1, _product * _temp)


print(_calc(5, 1))
