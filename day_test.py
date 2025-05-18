
import datetime

year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入几日："))

date1 = datetime.date(year=year, month=month, day=day)

print(type(date1))

date2 = datetime.date(year=year, month=1, day=1)
print(type(date2))

tty = date1 - date2
print(type(tty))
print(type(year))

print(tty)

