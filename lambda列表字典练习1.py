#lambda 列表元素的长度排序练习

animals = ['pig', 'cat', 'orange', 'grap', 'dog', 'banannna' ]

sorted_animals = sorted(animals, key=lambda s: len(s))

print(sorted_animals)

print(sorted(animals))

#字典按照value 排序

stu_height = {'kate':180, 'lily':165, 'tim':156, 'jack':182, 'sophia':173}

sorted_height = sorted(stu_height.items(), key=lambda item: item[1])

print(sorted_height)