
#不改变原列表顺序去重


list1 = [1, 3, 6, 89, 3, 22, 1, 56, 89]


#set 函数可以去重，但是会改变列表元素的顺序
list2 = set(list1)
print(list2)

#定义一个空列表list3
list3 = []

for i in list1:
    if not i in list3:
        list3.append(i)

print(list3)

