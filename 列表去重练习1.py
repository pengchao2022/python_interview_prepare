

#去除列表中重复的原色并保持元素的顺序不变

my_list1 = [55, 77, 4, 55, 90, 77, 5, 66, 5]

#定义一个空的列表my_list2

my_list2 = []

#将my_list1中的元素插入mylist2

for n in my_list1:
    if not n in my_list2:
        my_list2.append(n)

print(my_list2)