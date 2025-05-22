
def remove_odd(args):
    i = 0
    while i < len(args):
        if args[i] % 2 == 1:
            args.pop(i)
        else:
            i += 1

    return args

list1 = [11, 22, 33, 44, 55, 77, 66, 88, 99]

print(remove_odd(list1))