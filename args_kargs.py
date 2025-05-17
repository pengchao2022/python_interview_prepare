
def demo(*args):
    print(args)
    print(type(args))

demo(1,2,3,4,6)


def demo2(**kargs):
    print(kargs)
    print(type(kargs))

#key value 形式
demo2(a=6,b=8)

def demo3(*args,**kargs):
    print(args)
    print(kargs)

demo3(1,6,a=9,b=88)


