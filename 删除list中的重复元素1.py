
list1 = [77, 90, 90, 87, 65, 77, 45, 45]

list2 = []

for x in list1:
    if not x in list2:
        list2.append(x)

print(f"去重后的列表为：{list2}")