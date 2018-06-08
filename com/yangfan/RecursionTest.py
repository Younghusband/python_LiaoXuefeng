def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# print(fact(100))

def fact_tail(n, src):
    if n == 1:
        return src
    return fact_tail(n - 1, n * src)


print(fact_tail(100, 1))

# print 1,3,5,7...
# 差一个汉诺塔要写  还没写

n = 1
while n <= 50:
    if n == 50:
        print(2 * n - 1, end = '')
    else:
        print(2 * n - 1, ",", end = '')
    n += 1

print()  # 换行
print(list(range(1, 100, 2)))
