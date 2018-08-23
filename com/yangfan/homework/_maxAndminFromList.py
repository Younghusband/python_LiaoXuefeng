from collections import Iterable


def find_min_max(L):
    # 判断是否为None [] 以及不可迭代对象
    if L is None or L == [] or not isinstance(L, Iterable):
        return None, None
    _min = L[0]
    _max = L[0]
    for i, v in enumerate(L):
        if v > _max:
            _max = v
        if v < _min:
            _min = v
    return _min, _max


L = [-1, 2, 3, 4, 5, 6, -7]

print(find_min_max(L))
print(find_min_max(['a', 'b', 'c']))
print(find_min_max([]))
print(find_min_max(1234))
print(find_min_max([123, 5, 67, 9, 89]))
print(find_min_max(['abc', 'edf', 'abd', 'jnk']))
