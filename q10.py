# _*_ coding: utf-8 _*_

"""题目：暂停一秒输出，并格式化当前时间。"""

import datetime as d
import time
for i in range(5):
    t = d.datetime.today()
    print(t.isoformat(), t.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
