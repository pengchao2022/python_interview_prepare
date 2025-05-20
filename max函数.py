#打印出列表里面的最大元素


def my_max(args):
    max_nu = args[0]
    for n in args:
        if n > max_nu:
            max_nu = n
                                                  
    print(f"最大的元素是{max_nu}")

list1 = [99, 678, 3]

my_max(list1)

#使用max函数打印最大值
print(list1)

print(max(list1))

print(len(list1))

print(min(list1))