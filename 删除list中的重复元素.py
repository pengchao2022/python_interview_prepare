
list1 = [98, 67, 5, 87, 33, 9, 33, 67]

list2 = []

for i in list1:
    if not i in list2:
        list2.append(i)

print(list2)