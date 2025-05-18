
def bubble(mylist):
    #i 循环次数
    for i in range(0, len(mylist)-1):
        #j 列表的下标或索引
        #对程序进行优化使用-i 次， 当然不减i也可以
        for j in range(0, len(mylist)-1-i):
        
            if mylist[j] > mylist[j+1]:
                #互换一下值 类似a,b = b,a
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
    print(mylist)

mylist1 = [77, 98, 4, 6, 675, 1, 43, 29, 201]
mylist2 = [765, 331, 7, 65, 43, 2, 109, 1, 3]

bubble(mylist1)
bubble(mylist2)