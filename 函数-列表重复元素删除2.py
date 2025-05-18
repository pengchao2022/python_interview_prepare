
def remove_du(mylist):
    my_new_list = []
    for x in mylist:
        if not x in my_new_list:
            my_new_list.append(x)

    print(f"去重后的列表为：{my_new_list}")

mylist1 = [88, 99, 66, 66, 88, 99]

mylist2 = [99, 99, 77, 66, 66, 56, 56, 77]
remove_du(mylist1)

remove_du(mylist2)