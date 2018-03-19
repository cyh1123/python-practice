# _*_ coding: utf-8 _*_

"""题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。"""
from math import sqrt


def primefactor(n):
    assert isinstance(n, int) and n > 0, 'TypeError'
    m = n
    print('%s = ' % n, end='')
    while True:
        for i in range(2, int(sqrt(m)+2)):
            if m % i == 0:
                m //= i
                print('%s * ' % i, end='')
                break
            if i == int(sqrt(m)+1):
                print(m)
                if m == n:
                    print('this is prime number!')
                return

primefactor()