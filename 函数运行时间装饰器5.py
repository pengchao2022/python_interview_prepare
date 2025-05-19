#编写一个判断函数运行时间的装饰器

import time

def outer(fn):
    def wrapper(*arg, **kwargs):
        start = time.time()
        ret = fn(*arg, **kwargs)
        end = time.time()
        print(end - start)
        return ret
    return wrapper

@outer
def test():
    time.sleep(3)

test()