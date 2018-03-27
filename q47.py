# -*- coding: UTF-8 -*-

"""题目：两个变量值互换。"""

def exchange(x, y):
    x, y = y, x
    return x, y

print(exchange('a', 26))