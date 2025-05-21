
#将如下字典按照年龄排序 

d1 = [
    {'name':'alice', 'age':38},
    {'name':'bob', 'age':18},
    {'name':'Carl', 'age':28},
]

ret = sorted(d1,key=lambda x:x['age'])

print(ret)