#统计列表当中元素出现的次数并返回字典

def count_number(items): #items 代表列表
    #定义一个空字典用于存放返回值
    d = {}
    #for循环遍历列表
    for item in items:
        #统计列表中的数字，判断下，不是数字的话将不进行统计
        if isinstance(item, (int, float)):
            d[item] = d.get(item, 0) + 1
    return d

ret = count_number([1,8,8,8,9,9,9,9,9,9,9,'u','i'])

print(ret)