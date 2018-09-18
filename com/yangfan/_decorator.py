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
import functools

def timer(para):
    def decorator(func):  # 这步
        @functools.wraps(func)      # 将func的相应属性赋值给wrapper
        def wrapper(*args, **kwargs):
            print('%s is fucking %s!' % (func.__name__ ,para))
            start = time.time()
            res = func(*args, **kwargs)
            stop = time.time()
            print('%s over %s!' % (func.__name__ ,para))
            print('cost: %s s' % (stop - start))
            return res
        return wrapper  # 这个相当于是被包装了一层的原函数
    return decorator


@timer('Lan')
def test(*aaa):    # 这个地方如果写非可变参数的话，调用的时候也需要传入参数
    time.sleep(2)  # 表示目标函数实际处理流程
    return 'Yangfan'   # 执行到最后才会打印


# test = timer(test) #6  传入原函数
print(test())  #7   调用包装好的函数

print('-----------')
print(test.__name__)    # 在functools的wraps操作之前会打印wrapper




