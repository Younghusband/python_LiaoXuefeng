import time

def timer(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s 开始执行... ' % text)
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time()
            print('%s 耗时 %s s' % (text,(end - start)))
            return res
        return wrapper
    return decorator

# @timer('无敌YF')
def process():
    time.sleep(2)
    return 'OMG'

timer = timer('无敌YF')
process = timer(process)

print(process())

print(process.__name__)
