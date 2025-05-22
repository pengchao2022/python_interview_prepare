#检测字符串中只含有数字

def is_all_digits(s:str) -> bool: #->函数类型注释 表示返回值为 bool 型
    if not s:
        return False  #空字符串返回false
    for char in s:
        if not ('0' <= char <= '9'):
            return False
        
    return True

str1 = "123456"
str2 = '123ert56'
str3 = ""
str4 = '999'

print(is_all_digits(str1))

print(is_all_digits(str2))

print(is_all_digits(str3))

print(is_all_digits(str4))





