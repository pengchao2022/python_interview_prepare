#lambda filter 过滤字符串长度

animals = ['dog', 'orange', 'elephant', 'panda', 'mouse', 'ji']

filter_ani = list(filter(lambda s: len(s) > 3, animals))

print(filter_ani)

filter_ani_1 = list(filter(lambda s: len(s) < 3, animals))

print(filter_ani_1)