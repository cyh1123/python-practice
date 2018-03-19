# _*_ coding: utf-8 _*_

"""题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。"""
from math import sqrt


def factor(num):
    assert isinstance(num, int) and num > 0, 'wrong number'
    L = []
    for i in range(1, int(sqrt(num) + 1)):
        if num % i == 0:
            j = num // i
            L.extend([i, j])
    return sorted(list(set(L)))[:-1]


for m in range(1, 111111):
    if m == sum(factor(m)):
        print(m, '\n', factor(m))




def otherway():
    for i in range(1, 111111):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        if s == i:
            print(i)


otherway()