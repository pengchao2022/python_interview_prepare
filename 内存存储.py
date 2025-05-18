
#不可变类型的数据：int, float, str, tuple


#可变类型： list, dict, set

a = 78
b = 90

a,b = b,a

print(f"a={a}")
print(f"b={b}")

list1 = [45, 78, 3, 56, 12, 900, 4, 2, 200]

for i in range(0, len(list1)-1):
    if list1[i] > list1[i+1]:
        list1[i],list1[i+1] = list1[i+1],list1[i]

print(list1)

def bubble(mylist):

    for i in range(0, len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]

    print(list1)

bubble(list1)

print(len(list1))




