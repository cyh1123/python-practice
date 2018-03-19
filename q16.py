# _*_ coding: utf-8 _*_

"""题目：输出指定格式的日期。"""

from datetime import datetime


date_string = '2018/3/12'

# 按指定格式输入日期
mydate = datetime.strptime(date_string, '%Y/%m/%d')
print(mydate)

# 输出指定格式的日期
print(mydate.strftime('%Y %m %d'))

