

def str_to_nu(args):
    num = 0
    for char in args:
        digit = ord(char) - ord('0')
        num = num*10 + digit

    print(f"转换成整型数字为：{num}")

str1 = "12345689"

str_to_nu(str1)

