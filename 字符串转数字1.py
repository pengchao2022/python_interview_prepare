
def str_to_nu(args):
    num = 0
    for char in args:
        digit = ord(char) - ord('0')
        num = num*10 + digit
    print(f"转换为整型数字为：{num}")

str1 = "123456789"

str_to_nu(str1)