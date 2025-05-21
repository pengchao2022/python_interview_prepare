
def list_combine(arg1, arg2):
    arg1.extend(arg2)
    return arg1


list1 = [9, 8, 7, 6]

list2 = [99, 88, 77]

print(list_combine(list1, list2))
