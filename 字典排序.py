d1 = [
    {'name':'alice', 'age':56},
    {'name':'lily', 'age':28},
    {'name':'kate', 'age':67}
]

result = sorted(d1,key=lambda x:x['age'])

print(result)


d2 = [
    {'name':'zhangsam', 'age':15},
    {'name':'lisi', 'age':45},
    {'name':'wang5', 'age':11}
]

ff = sorted(d2,key=lambda x:x['age'])

print(ff)