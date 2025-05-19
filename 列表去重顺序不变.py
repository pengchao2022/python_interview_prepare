
def re_du(mylist):
    new_list = []
    for x in mylist:
        if not x in new_list:
            new_list.append(x)

    print(f"去重后的新列表为:{new_list}")

list1 = [99, 88, 99 ,88, 67, 7, 45, 2, 45]

re_du(list1)