# _*_ coding: utf-8 _*_

"""题目：判断101-200之间有多少个素数，并输出所有素数。"""

from math import sqrt


def isprimenum(num):
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return 0
    return 1

def pickfrom(a, b):
    print('区间[%s, %s]' % (a, b))
    tol = 0
    for n in range(a, b+1):
        if isprimenum(n):
            tol += 1
            print('第%s个素数：%s' % (tol, n))

pickfrom(101, 200)

