#将字典按照 value 值进行排序

dict1 = {'a':24, 'g':55, 'k':8, 'y':67, 'r':33}

#print(dict1.items())

#按照value进行排序
ret = sorted(dict1.items(), key=lambda x: x[1])

print(ret)

dict2 = {66:'jim', 7:'allen', 88:'tianya'}

#按照key进行排序
result1 = sorted(dict2.items(), key=lambda x: x[0])

print(result1)

#字典推导式---将结果返回为字典格式

dict_1 = {key:value for key,value in ret}

print(dict_1)

dict_2 = {key:value for key,value in result1}

print(dict_2)

