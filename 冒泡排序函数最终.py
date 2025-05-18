
def bubble(mylist):
    #i 循环次数
    for i in range(0, len(mylist)-1):
        #j 列表的下标或索引
        for j in range(0, len(mylist)-1):
            if mylist[j] > mylist[j+1]:
                #互换一下值 类似a,b = b,a
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
    print(mylist)

mylist = [77, 98, 4, 6, 675, 1, 43, 29, 201]

bubble(mylist)