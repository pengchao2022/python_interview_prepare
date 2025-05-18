#打印列表里特定元素的索引

mylist = ['dog', 'cat', 'bees', 'pig', 'bird']

#打印所有的元素和对应的索引

for index, value in enumerate(mylist):
    print(index, value)


#打印特定元素的索引 如：pig
target = 'pig'
for index,value in enumerate(mylist):
    if value == target:
        print(f"{target}对应的索引值为：{index}")


