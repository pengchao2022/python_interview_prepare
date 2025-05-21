
'''
mylist =  [5, 8, 9, 8, 6, 7, 1, 111]

list1 = []

for i in mylist:

    if i % 2 != 0:
        list1.append(i)

print(list1)

'''

#用函数实现
'''
def odd_list(args):
    new_list = []
    for i in args:
        if i % 2 != 0:
            new_list.append(i)
    print(f"奇数列表为：{new_list}")

list1 = [1, 5, 8, 6, 57, 55, 132, 33]

list2 = [1, 77, 99, 54, 88, 300, 400]

odd_list(list1)

odd_list(list2)

'''
#用函数实现偶数列表

def even_list(args):
    new_even_list = []
    for i in args:
        if i % 2 == 0:
            new_even_list.append(i)

    print(f"新生成的偶数列表为：{new_even_list}")


list1 = [99, 88, 77, 66, 55, 44, 33, 22, 11]

even_list(list1)