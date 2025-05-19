

'''
a, b, c, d = 10, 200, 45, 500

print(a)
print(b)
print(c)
print(d)

'''

'''
a, b, c, d = 87, 99, 53, 100

print(a)
print(b)
print(c)
print(d)
'''

a, b, c, d = 2, 2, 1000, 1000

print(a is b, c is d)

def foo():
    e = 2000
    f = 2000
    print(e is f, e is d)

    g = 2
    print(g is a)


foo()


