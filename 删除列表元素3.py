def remove_even(args):
    i = 0
    while i < len(args):
        if args[i] % 2 == 0:
            args.pop(i)
        else:
            i += 1
    return args


list1 = [99, 88, 66, 77, 55, 44, 33, 22]

print(remove_even(list1))