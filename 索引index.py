str1 = "I Love China"

l1 = str1.split(' ')

print(l1)

for index, value in enumerate(l1):
    print(index,value)

l2 = list(str1)

for index, value in enumerate(l2):
    print(index,value)

l3 = list(str1)

for j in enumerate(l3):
    print(j)


l4 = list(str1)

for u in l4:
    print(u)
    