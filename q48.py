# -*- coding: UTF-8 -*-

"""题目：数字比较。"""

def compare(x, y):
    try:
        if x < y:
            print('%s is smaller than %s' % (x, y))
        elif x == y:
            print('%s is equal to %s' % (x, y))
        elif x > y:
            print('%s is greater than %s' % (x, y))
    except:
        print('unknown')


compare(46, 'q')
