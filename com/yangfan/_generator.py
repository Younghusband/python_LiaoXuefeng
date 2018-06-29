L = [n * n for n in range(10)]

print('-------------------\n', L)

S = (x * x for x in range(10))

print('-------------------\n', S)  # tuple就打印不出来

print(next(S))  # 每次调用next(S) 就会调用S的generator
print(next(S))
print(next(S))
print(next(S))
print(next(S))
print(next(S))
print(next(S))
print(next(S))
print(next(S))
print(next(S))
# print(next(S))    # 到这里会 StopIteration

# 然而实际应用的时候我们不需要不停的next(), for循环即可
print('----------------------------------')

X = (x * x for x in range(10))  # 这个地方如果循环S 是没数的，因为S已经到底了
for i in X:
    print(i)

print('----------------------------------')

def odd():
    print('step1...')
    yield 1
    print('step2...')
    yield 2
    print('step3...')
    yield 3


X = odd()
print(next(X))  # next(X) 会逐次返回1,2,3
print(next(X))
print(next(X))

# 请注意区分普通函数和generator函数，普通函数调用直接返回结果
# generator函数的“调用”实际返回一个generator对象
