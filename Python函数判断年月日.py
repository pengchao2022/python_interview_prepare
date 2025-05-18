
#使用python语言输入年月日，判断这一天是这一年中的第几天 

import datetime

def day_of_year():
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入几日："))

    date1 = datetime.date(year=year, month=month, day=day)
    date2 = datetime.date(year=year, month=1, day=1)
     
    ret = (date1 - date2).days + 1

    print(f"这是一年中的第{ret}天")

day_of_year()