#检测数字字符串是不是纯数字 

def is_all_digits(s:str) -> bool:
    if not s:
        return False
    
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return True

str1 = '89007uiii'

str2 = '76665566'

str3 = '342567'

print(is_all_digits(str1))

print(is_all_digits(str2))

print(is_all_digits(str3))

