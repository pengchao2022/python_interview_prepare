#打印特定元素的索引

mylist = ["apple", "banana", "orange", "tomato"]

#打印全部元素和索引

for index, value in enumerate(mylist):
    print(index,value)

#打印特定元素的如orange的索引
target = "tomato"
for index, value in enumerate(mylist):
    if value == target:
        print(f"{target}对应的索引号为：{index}")



