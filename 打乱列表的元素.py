
import random

def da_luan(args):
    random.shuffle(args)
    return args


list1 = [1, 2, 3, 4, 5, 6]

list2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]

list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

list4 = ['kate', 'lily', 'Tim', 'george']

print(da_luan(list1))

print(da_luan(list2))

print(da_luan(list3))

print(da_luan(list4))

