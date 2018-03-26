# -*- coding: UTF-8 -*-

"""题目：求输入数字的平方，如果平方运算后小于 50 则退出。"""

def mysquare():
    n = float(input('input a number: '))
    while True:
        if n**2 < 50:
            break
        print('the square of the number: %s' % n**2)
        n = float(input('input again: '))

mysquare()