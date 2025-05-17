strs = 'I like python and java'

one = strs.find('n')

print(one)

two = strs.rfind('n')

print(two)

three = strs.rfind('K')

print(three)

four = strs.find('java')

print(four)

char_list = list(strs)
print(char_list)


for index, value in enumerate(char_list):
    print(f"索引 {index} 对应的元素是: {value}")

