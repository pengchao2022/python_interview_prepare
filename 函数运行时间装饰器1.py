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
    time.sleep(6)

test()