
name = 'Sophia'

age = 34

height = 182

weight = 65.5555

#输出方法一

print("姓名为：%s" % name)

print("年龄为：%d" % age)

print("身高为： %d" % height)

print('体重为： %.2f' % weight)

#输出格式化方法二

print(f"姓名为：{name}")

print(f"年龄为：{age}")

print(f"身高为：{height}")

#注意体重保留两位小数
print(f"体重为：{weight: .2f}")


