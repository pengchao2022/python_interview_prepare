#素数是除了1和本身外，不能被其他数整除

num = int(input("请输入一个正整数："))

for i in range(2, num):
    if num % i == 0:
        print(f"{num}不是素数")
        break

else:
    print(f"{num}是素数")