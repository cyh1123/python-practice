# -*- coding: UTF-8 -*-

"""题目：统计 1 到 100 之和。"""

def mycount(begin, end):
    s = sum(range(begin, end + 1))
    return 'the sum is: %s' % s

print(mycount(1, 100))