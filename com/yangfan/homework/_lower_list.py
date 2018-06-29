L1 = ['Hello', 'World', 18, 'Apple', None]


def _lower_func(_list):
    _return_list = []
    for v in _list:
        if isinstance(v, str):
            _return_list.append(v.lower())
        else:
            _return_list.append(v)
    return _return_list


print(_lower_func(L1))

print('----------------------')

print(L1)


L2 = []
L2 = [v.lower() for v in L1 if isinstance(v, str)]

# L2 = [L2.append(v.lower()) for v in L1 if isinstance(v, str)]  # 这么写是错的

# 我估计 for 语句前面的整体会作为一个值注入， 所以 L2.append(v.lower()) 返回了None 注入了L2

print(L2)
