#过滤偶数

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

odd = list(filter(lambda y: y % 2 != 0, numbers))

print(odd)