#书写最小值函数

def nu_min(args):

    min_ = args[0]

    for n in args:
        if n < min_:
            min_ = n

    print(f"列表中最小的值为{min_}")

list1 = [7, 89, 65, 45, 7600]

print(list1)
nu_min(list1)
