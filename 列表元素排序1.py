#将列表元素去重后按照升序，降序排列

mylist = [99, 88, 67, 88, 99, 6, 7, 4, 12, 4]

#打印列表的长度
print(f"原始列表的长度为：{len(mylist)}")

#将列表去重
my_new_list = set(mylist)

print(f"去重后的列表为:{my_new_list}")
print(f"去重后列表的长度为：{len(my_new_list)}")

#将新列表按照升序排列
sorted_list = sorted(my_new_list)

#打印升序列表
print(f"升序排列后的列表为：{sorted_list}")

#将新列表按照降序排列
r_sorted_list = sorted(my_new_list, reverse=True)

print(f"按照降序排列的列表为：{r_sorted_list}")

print(r_sorted_list(88))


