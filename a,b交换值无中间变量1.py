
a = 50
b = 60

#方法一
'''
a,b = b,a
print(a, b)

'''

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




