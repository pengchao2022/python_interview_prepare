
def check_nu(arg1,arg2):
    same_nu_list = []
    different_nu_list = []
    for i in arg1:
        if i in arg2:
            same_nu_list.append(i)
    
    for j in arg1:
        if not j in arg2:
            different_nu_list.append(j)
    for k in arg2:
        if not k in arg1:
            different_nu_list.append(k)
    
    print(f"相同的元素为：{same_nu_list}")
    print(f"不同的元素为：{different_nu_list}")


list1 = [9, 8, 7, 99, 101, 98]
list2 = [1, 9, 7, 101]
list3 = [88, 99, 6]

check_nu(list1, list2)

check_nu(list1, list3)
