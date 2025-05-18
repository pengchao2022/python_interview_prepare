#将字符串处理成字典

str1 = "k:1 |k1:2|k2:3|k3:4"

def str_to_dict(str1):

    dict1 = {}

    for items in str1.split('|'):
        key, value = items.split(':')
        dict1[key] = int(value)
    return dict1
    
ret = str_to_dict(str1)

print(ret)
