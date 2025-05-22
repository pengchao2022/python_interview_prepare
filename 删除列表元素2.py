def remove_even(args):
    i = 0
    while i < len(args):
        if args[i] % 2 == 0:
            args.pop(i)   # 删除后不递增索引
        else:
            i += 1        # 保留元素时递增索引
    return args

list1 = [88, 99, 77, 84]
print(remove_even(list1))  # 输出: [99, 77]