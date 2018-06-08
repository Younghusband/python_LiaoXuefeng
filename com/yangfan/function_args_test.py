if 1 == 1:
    name = "LL"

# print(name)

for n in range(10):
    arg1 = n  # 0 遍历到9


# print(arg1)


def test():
    print("into test")


test()


# 默认参数


def power(x, n = 2):
    s = 1
    while n >= 1:
        s *= x
        n -= 1
    return s


# print(power(3))


# []是可变参数，空参调用的时候会有问题


def add_end(list1 = []):
    list1.append('END')
    return list1


print(add_end([1, 2, 3, 4]))
print(add_end([1, 2, 3, 4]))

print(add_end())  # [END]
print(add_end())  # [END,END]

print('\n>>>>>>>> safe method below <<<<<<<<\n')


def add_end_safe(list1 = None):  # 这种就没有上面的隐患
    if list1 is None:
        list1 = []
    list1.append("END")
    return list1


print(add_end_safe())  # [END]
print(add_end_safe())  # [END]


def and_pow(numbers):  # input可变类型
    sums = 0
    for i in numbers:
        sums = sums + i * i
    return sums


print(and_pow([1, 2, 3]))


def and_pow_pro(*numbers):
    sums = 0
    for i in numbers:
        sums = sums + i * i
    return sums


print(and_pow_pro(1, 2, 3))  # 简化调用
print(and_pow_pro())

aaa = [1, 2, 3]
print(and_pow(aaa))
print("----------")
# print(and_pow(*aaa))   # 这行会报错，方法不能传入可变参数
print(and_pow_pro(*aaa))
# print(and_pow(aaa[1], aaa[2], aaa[3]))  # 这行也会报错
print(and_pow_pro(aaa[0], aaa[1], aaa[2]))

extra = {'address': 'Hangzhou', 'sex': 'F'}


def person(name1, age, **kw):
    print('name:', name1, 'age:', age, 'other:', kw)  # 必须','分隔 而不能用'+'


person('杨帆', 3)  # 关键字参数的几种调用方法
person('杨帆', 3, address = 'Hangzhou', sex = 'F')
person('黄翔', 3, Address = extra['address'], Sex = extra['sex'])
person('黄翔', 3, **extra)

'''  
  进阶版本的person

'''
print("\n------------进阶版本------------\n")


def person_check(name, age, **kw):
    if 'city' in kw:
        print('city in kw')
        pass
    if 'job' in kw:
        print('job in kw')
        pass
    print('name:', name, 'age:', age, 'others:', kw)


cityNjob = {'city': '杭州', 'job': '码农'}

person_check("杨欢", 3)
person_check('黄翔', 3, **cityNjob)

'和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。 '


def person_ness(name, age, *, city, job):  # 缺少 *的话，city和job被视为位置参数
    print(name, age, city, job)


# person_ness('yangfan', 3, city = 'HZ')  # 缺少job参数，该行会报错
person_ness('yangfan', 3, city = 'HZ', job = '码农')

' 参数的组合 '


def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')  # kw为空
f1(1, 2, {'city': 'hangzhou'})  # 会把这个dict 传进c... 这点很无语， 必选参数必须得有，跳不过去

' 参数的玩法太过于灵活了，这里就不展开了，展开我也会转头就忘了 '

print("-------------下面是作业-------------")


def product(*args):
    if args == ():
        raise TypeError('杨帆傻逼啦！')
    ori = 1
    for e1 in args:
        ori *= e1
    return ori


t1 = (2, 10)

print(product())  # 故意让报错
print(product(1))
print(product(1, 2, 3))
print(product(1, 2, 0))
print(product(t1))  # 会将该tuple作为第一个参数。。很尴尬
