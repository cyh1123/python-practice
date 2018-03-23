# -*- coding: UTF-8 -*-

"""题目：求100之内的素数。"""
from math import sqrt


def primenumber(n, m):
    assert isinstance(n,int) and isinstance(m, int) and (0 < n < m), 'wrong number!'
    for i in range(n, m + 1):
        for j in range(2, int(sqrt(i)+2)):
            if i % j == 0:
                break
            if j == int(sqrt(i)+1):
                print(i)


primenumber(1, 100)