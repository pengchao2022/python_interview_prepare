
def choose_sort(mylist):
    for i in range(len(mylist)-1):
        m = i
        for j in range(i+1, len(mylist)):
            if mylist[j] < mylist[m]:
                m = j
        temp = mylist[i]
        mylist[i] = mylist[m]
        mylist[m] = temp

    print(mylist)

mylist1 = [66, 78, 3, 45, 23, 4, 7, 56]

choose_sort(mylist1)