# 装饰器 对已有函数进行包装，传入目标函数的__name__ 来实现装饰
# 类似java中的aop的那种感觉
#   1. 不能修改被装饰的函数的源代码
#   2. 不能修改被装饰的函数的调用方式
#   3. 满足1,2的情况下给程序增添功能
#


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')


now()

import time

def timer(func):  # 5
    def deco(*args,**kwargs):
        print('%s is running!' % func.__name__)
        start = time.time()
        func(*args,**kwargs)
        stop = time.time()
        print('%s over!' % func.__name__)
        print('cost: %s s' % (stop - start))
    return deco    # 这个相当于是被包装了一层的原函数

@timer
def test(para):
    time.sleep(2)  # 表示目标函数实际处理流程


# test = timer(test) #6  传入原函数
test() #7   调用包装好的函数
