# a,b 进行交换无中间变量

a = 20
b = 30

#方法一
#a,b = b,a
#print(a, b)

#方法二
'''
a = a + b
b = a - b
a = a - b

print(a, b)
'''

#方法三

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

