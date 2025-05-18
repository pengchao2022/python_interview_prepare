#使用函数进行冒泡排序

def bubble(mylist):
    for j in range(0, len(mylist)-1):
        if mylist[j] > mylist[j+1]:
            mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
    print(mylist)

mylist = [66, 78, 4, 54, 43, 23, 7, 1]

bubble(mylist)
bubble(mylist)
bubble(mylist)
bubble(mylist)
bubble(mylist)
bubble(mylist)
bubble(mylist)