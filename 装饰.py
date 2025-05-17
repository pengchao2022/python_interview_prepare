
def outer():
    def inner():
        print('inner',end=" ")
    print('outer',end=" ")
    return inner

outer()