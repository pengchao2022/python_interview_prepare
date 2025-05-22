
name = "Kate"

age = 24

height = 182

weight = 45.5333333

#方法一 % 格式化
print("姓名为：%s" % name)
print("年龄为：%d" % age)
print("身高为：%d" % height)

#小数点后保留两位
print("体重为：%.2f" % weight)

#方法二 f 格式化

print(f"姓名为：{name}")
print(f"年龄为：{age}")
print(f"身高为：{height}")
print(f"体重为：{weight: .2f}")

