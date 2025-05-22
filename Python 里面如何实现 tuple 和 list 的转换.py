
#Python 里面如何实现 tuple 和 list 的转换

list1 = ['a', 'b', 'c', 'd']

tuple1 = (77, 88, 55, 33)

my_list = list(tuple1)

print(my_list)

my_tuple = tuple(list1)

print(my_tuple)