
import random

def mk_change(mylist):
    random.shuffle(mylist)
    print(f"打乱后的列表为：{mylist}")


list1 = ['a', 'b', 'c', 'd', 'e', 'f']

list2 = [98, 78, 56, 5, 77, 45, 1, 4, 3]

mk_change(list1)

mk_change(list2)